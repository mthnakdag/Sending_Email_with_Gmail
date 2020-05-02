def send_mail(text=None, subject="",
              from_email=None, to_email=None,
              html = None,img_path=None):
    
    """
    text is input email body -- str
    subject is input email subject -- str
    from_email which mail addresses -- str
    to_email send email who . You can change some code parts to_email convert a list with (", ").join format --str
    html if your body part is not plain text hyper text also you can send html --str
    img_path if you can adding a image give image path -- str
    """
    
    assert isinstance(text,str) or isinstance(html,str)
    assert isinstance(from_email, str)
    assert isinstance(to_email, str)
    
    msg = MIMEMultipart("alternative")# Creating a msg object suitable for smtp format
    msg["From"] = from_email 
    msg["To"] = to_email
    msg["Subject"] = subject
    

    if text is not None:                 # if text coming
        txt_part = MIMEText(text, "plain")
        msg.attach(txt_part) #attaching body
        
    if html is not None:                 # if html coming
        html_part = MIMEText(html,"html")
        msg.attach(html_part)            # attaching body
        
    if img_path is not None:             # if image coming
        image = MIMEImage(open(img_path, "rb").read(), name= os.path.basename(img_path))
        msg.attach(image)                # attaching image
        
    msg_str = msg.as_string() # msg convert the string format
    
    
    with smtplib.SMTP(host= HOST, port= PORT) as server: #server communication
        server.ehlo()
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.sendmail(from_email, to_email, msg_str)

