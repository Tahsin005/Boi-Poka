from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DepositForm
from .models import Transaction
from django.urls import reverse_lazy
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
def send_transaction_email(user, amount, subject, template):
    #email send 
    mail_subject = "Deposit Message"
    message = render_to_string(template, {
        'user': user,
        'amount': amount,
    })
    send_email = EmailMultiAlternatives(subject, '', to={user.email})
    send_email.attach_alternative(message, "text/html")
    send_email.send()
# Create your views here.
class DepositView(CreateView, LoginRequiredMixin):
    template_name = 'transaction/deposit.html'
    model = Transaction
    form_class = DepositForm
    success_url = reverse_lazy('home')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs
    
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount 
        account.save(
            update_fields=[
                'balance'
            ]
        )
        send_transaction_email(self.request.user, amount, "Successfully Deposited On Boi Poka", "transaction/deposit_email.html")
        return super().form_valid(form)


class TransactionReportView(ListView, LoginRequiredMixin):
    model = Transaction
    template_name = 'transaction/report.html'
    
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(
            user=self.request.user.account
        )
        
        return queryset
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['transactions'] = self.get_queryset()
        
        return context