import pyautogui
import time


gmail_file_path = 'gmail.txt'  
link_file_path = 'links.txt'    

time.sleep(5)  # delay for u open gmail manually


with open(gmail_file_path, 'r') as file:
    emails = [email.strip() for email in file.readlines()]

with open(link_file_path, 'r') as file:
    links = [link.strip() for link in file.readlines()]

if len(emails) != len(links):
    print("Error: Number of emails does not match number of links.")
else:

    for email, link in zip(emails, links):
        
        pyautogui.click(x=30, y=205)  # change it for coordinate of 'Compose' 
        time.sleep(0.2)  

        
        if '@' in email:
            
            local_part, domain_part = email.split('@', 1)  

            pyautogui.write(local_part) 
            pyautogui.hotkey('altright', 'q')  
            pyautogui.write(domain_part)  
        else:
            print(email+" is not valid") 
        time.sleep(0.5)
        
        pyautogui.click(x=1753,y=488)  #click for subject


        
        subject = "Welcome to our TEDx event"
        pyautogui.write(subject)

        pyautogui.press('tab')  #for type in body


        
        body_text = f"Bu senin QR kodun:\n\n{link}"
        pyautogui.write(body_text)

        
        pyautogui.hotkey('ctrl', 'enter')
        time.sleep(0.5)

