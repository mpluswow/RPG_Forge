
# Flask Deployment with Gunicorn and Nginx

This guide covers deploying a Flask app using **Gunicorn** as the WSGI server and **Nginx** as a reverse proxy on an Ubuntu server.

---

## 1. Prepare the Server

### 1.1 Update the System
```bash
sudo apt update && sudo apt upgrade -y
```

### 1.2 Install Required Software
```bash
sudo apt install python3 python3-pip python3-venv nginx git && sudo apt install mysql-server libmysqlclient-dev pkg-config python3-dev build-essential -y
```

### 1.3 Create DB User

Log in to MySQL as root:

```bash
sudo mysql -u root -p
```
Create the DB User:

```sql
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
```

Grant privileges to all databases:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'your_username'@'localhost' WITH GRANT OPTION;
```

```sql
FLUSH PRIVILEGES;
```

```sql
exit
```
---

## 2. Set Up the Flask Application

### 2.1 Create the Project Directory
```bash
git clone https://github.com/mpluswow/RPG_Forge.git
```
```bash
cp -r RPG_Forge/GameServer gameServer
```
```bash
cd gameServer
```

### 2.2 Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2.3 Install Flask and Gunicorn
```bash
pip install flask gunicorn
```
### 2.4 Install Required Python Packages
```bash
pip install -r requirements.txt
```

### 2.5 Test the Flask App
Run the app:
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## 3. Configure Gunicorn

### 3.1 Test Gunicorn
Run Gunicorn:
```bash
/home/ubuntu/gameServer/venv/bin/gunicorn -w 3 -b 127.0.0.1:5000 app:app
```

---

## 4. Set Up Nginx

### 4.1 Configure Nginx
Create a new Nginx configuration file:
```bash
sudo nano /etc/nginx/sites-available/gameServer
```
Add this:
```nginx
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 4.2 Enable the Configuration
```bash
sudo ln -s /etc/nginx/sites-available/gameServer /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

---

## 5. Create a Systemd Service for Gunicorn

### 5.1 Create the Service File
```bash
sudo nano /etc/systemd/system/gameServer.service
```
Add this:
```plaintext
[Unit]
Description=Gunicorn instance to serve gameServer
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/home/ubuntu/gameServer
ExecStart=/home/ubuntu/gameServer/venv/bin/gunicorn -w 3 -b 127.0.0.1:5000 app:app
StandardOutput=append:/var/log/gameServer.log
StandardError=append:/var/log/gameServer_error.log

[Install]
WantedBy=multi-user.target
```

### 5.2 Set Permissions for Logs
```bash
sudo touch /var/log/gameServer.log /var/log/gameServer_error.log
sudo chown www-data:www-data /var/log/gameServer*.log
```

---

## 6. Adjust Permissions

### 6.1 Fix Permissions for the Project Directory
```bash
sudo chown -R www-data:www-data /home/ubuntu/gameServer
sudo chmod -R 755 /home/ubuntu/gameServer
```

### 6.2 Fix Parent Directory Permissions
```bash
sudo chmod 755 /home/ubuntu
```

---

## 7. Start and Enable the Service

### 7.1 Reload and Start the Service
```bash
sudo systemctl daemon-reload
sudo systemctl start gameServer
sudo systemctl enable gameServer
```

### 7.2 Check the Service Status
```bash
sudo systemctl status gameServer
```

---

## 8. Test the Setup
Visit:
```plaintext
http://<your-server-ip>
```

---

## 9. Set Up HTTPS with Certbot (Optional)

### 9.1 Install Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
```

### 9.2 Obtain and Configure SSL
```bash
sudo certbot --nginx
```

---

## 10. Verify Everything
1. Check your application:
    - HTTP: `http://<your-domain-or-ip>`
    - HTTPS: `https://<your-domain-or-ip>`
2. Ensure Gunicorn and Nginx are running:
```bash
sudo systemctl status gameServer
sudo systemctl status nginx
```

---

## Troubleshooting

### Check systemd Logs
```bash
journalctl -u gameServer
```

### Check Nginx Logs
```bash
sudo tail -f /var/log/nginx/error.log
```
