# This project is still in development!
*** ***
# Smart-biometrcis-entrance
We aim to make a project with biometric authentication linked to an sql database and an online website using pythonanywhere.
*** ***
# overview
*** ***
This project will include a dual authentication procedure using face recognition as well as vein authentication. 
The authentication will happen on a computer serving as a local server. The data ( pictures ) to authenticate will be gathered by an raspberry pi. The database for authentication wil be located on the local server because of safety and privacy concerns. 
The connection between the local server and the pi will be done by WiFi using a local mqtt message broker ( for scalability ). The data, after authentication, 
will be added to an online sql database provdided by python anywhere. In the cloud we will use Flask as our framework to run our website. The authentication for admin users on the website will consist out of a password, scanning of the ID and facial recognition.
Admin users will have the autority to see all the data and will have the power to add new, delete or promote users in the system.
