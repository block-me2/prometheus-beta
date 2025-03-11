import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional, List, Union

def send_email(
    sender_email: str, 
    sender_password: str, 
    recipient: Union[str, List[str]], 
    subject: str, 
    body: str, 
    smtp_server: str = 'smtp.gmail.com', 
    smtp_port: int = 587,
    cc: Optional[Union[str, List[str]]] = None,
    bcc: Optional[Union[str, List[str]]] = None
) -> bool:
    """
    Send an email using SMTP protocol.

    Args:
        sender_email (str): Email address of the sender
        sender_password (str): Password for the sender's email account
        recipient (str or List[str]): Email address(es) of recipient(s)
        subject (str): Subject line of the email
        body (str): Body text of the email
        smtp_server (str, optional): SMTP server address. Defaults to Gmail's SMTP.
        smtp_port (int, optional): SMTP server port. Defaults to 587 (TLS).
        cc (str or List[str], optional): Carbon copy recipient(s)
        bcc (str or List[str], optional): Blind carbon copy recipient(s)

    Returns:
        bool: True if email sent successfully, False otherwise

    Raises:
        ValueError: If input validation fails
        smtplib.SMTPException: If there's an error sending the email
    """
    # Validate inputs
    if not sender_email or not sender_password:
        raise ValueError("Sender email and password are required")
    
    if not recipient:
        raise ValueError("At least one recipient is required")
    
    # Normalize recipient, cc, and bcc to lists
    recipients = [recipient] if isinstance(recipient, str) else recipient
    cc_list = [cc] if isinstance(cc, str) else (cc or [])
    bcc_list = [bcc] if isinstance(bcc, str) else (bcc or [])
    
    # Validate email addresses (more robust regex check)
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    def validate_email(email):
        return email_regex.match(email) is not None
    
    # Check email format for all email addresses
    all_emails = recipients + cc_list + bcc_list + [sender_email]
    if not all(validate_email(e) for e in all_emails):
        raise ValueError("Invalid email address format")

    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = ', '.join(recipients)
        
        # Add CC if present
        if cc_list:
            message['Cc'] = ', '.join(cc_list)
        
        message['Subject'] = subject
        
        # Attach the body
        message.attach(MIMEText(body, 'plain'))
        
        # Combine all recipients for sending
        all_recipients = recipients + cc_list + bcc_list
        
        # Establish a secure session with Gmail's outgoing SMTP server using TLS
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable TLS encryption
            
            # Login to the server
            server.login(sender_email, sender_password)
            
            # Send the email
            server.sendmail(
                sender_email, 
                all_recipients, 
                message.as_string()
            )
        
        return True
    
    except (smtplib.SMTPException, ConnectionError) as e:
        # Log the error or handle it as needed
        print(f"Error sending email: {e}")
        return False