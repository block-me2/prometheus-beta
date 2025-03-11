import pytest
import smtplib
from unittest.mock import patch, MagicMock
from src.smtp_email_sender import send_email

class TestEmailSender:
    def test_valid_single_recipient_email(self):
        """Test sending email to a single recipient"""
        with patch('smtplib.SMTP') as mock_smtp:
            # Configure the mock to simulate successful email sending
            mock_instance = mock_smtp.return_value.__enter__.return_value
            
            result = send_email(
                sender_email='sender@example.com', 
                sender_password='password123', 
                recipient='recipient@example.com', 
                subject='Test Email', 
                body='This is a test email.'
            )
            
            assert result is True
            mock_instance.starttls.assert_called_once()
            mock_instance.login.assert_called_once_with('sender@example.com', 'password123')
            mock_instance.sendmail.assert_called_once()

    def test_multiple_recipients(self):
        """Test sending email to multiple recipients"""
        with patch('smtplib.SMTP') as mock_smtp:
            mock_instance = mock_smtp.return_value.__enter__.return_value
            
            result = send_email(
                sender_email='sender@example.com', 
                sender_password='password123', 
                recipient=['recipient1@example.com', 'recipient2@example.com'], 
                subject='Test Email', 
                body='This is a test email.'
            )
            
            assert result is True
            mock_instance.sendmail.assert_called_once()

    def test_email_with_cc_and_bcc(self):
        """Test sending email with CC and BCC"""
        with patch('smtplib.SMTP') as mock_smtp:
            mock_instance = mock_smtp.return_value.__enter__.return_value
            
            result = send_email(
                sender_email='sender@example.com', 
                sender_password='password123', 
                recipient='recipient@example.com', 
                subject='Test Email', 
                body='This is a test email.',
                cc='cc@example.com',
                bcc='bcc@example.com'
            )
            
            assert result is True
            mock_instance.sendmail.assert_called_once()

    def test_invalid_sender_email(self):
        """Test raising error for invalid sender credentials"""
        with pytest.raises(ValueError, match="Sender email and password are required"):
            send_email(
                sender_email='', 
                sender_password='password123', 
                recipient='recipient@example.com', 
                subject='Test Email', 
                body='This is a test email.'
            )

    def test_no_recipients(self):
        """Test raising error when no recipients are provided"""
        with pytest.raises(ValueError, match="At least one recipient is required"):
            send_email(
                sender_email='sender@example.com', 
                sender_password='password123', 
                recipient=[], 
                subject='Test Email', 
                body='This is a test email.'
            )

    def test_invalid_email_format(self):
        """Test raising error for invalid email addresses"""
        with pytest.raises(ValueError, match="Invalid email address format"):
            send_email(
                sender_email='invalid-email', 
                sender_password='password123', 
                recipient='recipient@example.com', 
                subject='Test Email', 
                body='This is a test email.'
            )

    def test_smtp_connection_failure(self):
        """Test handling of SMTP connection failures"""
        with patch('smtplib.SMTP') as mock_smtp:
            # Simulate SMTP connection failure
            mock_smtp.side_effect = smtplib.SMTPException("Connection failed")
            
            result = send_email(
                sender_email='sender@example.com', 
                sender_password='password123', 
                recipient='recipient@example.com', 
                subject='Test Email', 
                body='This is a test email.'
            )
            
            assert result is False