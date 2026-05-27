# Deployment Guide - Intrusive Thought Tracker

## Deployment Options

### Option 1: Docker (Recommended for Production)

#### Prerequisites
- Docker and Docker Compose installed
- Production OpenRouter API key
- Domain name (optional)

#### Steps
1. **Setup Environment Variables**
   ```bash
   cp .env.production .env
   # Edit .env with your production values
   ```

2. **Build and Deploy**
   ```bash
   docker-compose up -d --build
   ```

3. **Access Your App**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

#### For Production Domain
Update `.env`:
```
FRONTEND_URL=https://your-domain.com
BACKEND_URL=https://your-domain.com:5000
```

---

### Option 2: VPS Deployment (Linux)

#### Prerequisites
- Ubuntu 20.04+ or similar
- Node.js 18+
- Python 3.11+
- Nginx (optional but recommended)

#### Backend Setup
```bash
# Clone and setup
git clone <your-repo>
cd project/backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with production values

# Install and run with PM2
npm install -g pm2
pm2 start "uvicorn main:app --host 0.0.0.0 --port 5000" --name thought-tracker-api
pm2 startup
pm2 save
```

#### Frontend Setup
```bash
cd ../frontend
npm install
npm install -g pm2
pm2 start "npm start" --name thought-tracker-frontend
pm2 save
```

#### Nginx Configuration (Optional)
Create `/etc/nginx/sites-available/thought-tracker`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable and restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/thought-tracker /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

### Option 3: Cloud Platform Services

#### Heroku
1. Create `Procfile` in project root:
```
web: cd project/frontend && npm start
api: cd project/backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

2. Deploy:
```bash
heroku create your-app-name
heroku config:set AI_PROVIDER=openrouter
heroku config:set OPENROUTER_API_KEY=your_key
git push heroku main
```

#### Railway
1. Connect your GitHub repository
2. Set environment variables in Railway dashboard
3. Railway will auto-deploy on push

#### Render
1. Create two services: Web Service (frontend) and Private Service (backend)
2. Set environment variables
3. Connect GitHub repository

---

### Option 4: Static Frontend + Cloud Backend

#### Frontend (Vercel/Netlify)
1. Deploy frontend to Vercel or Netlify
2. Update `BACKEND_URL` environment variable

#### Backend (Render/Railway)
1. Deploy only backend to cloud platform
2. Configure CORS to allow your frontend domain

---

## Environment Variables Required

### Production Environment
```bash
AI_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-or-v1-your-production-key
FRONTEND_URL=https://your-domain.com
SECRET_KEY=your-32-character-secret-key
BACKEND_URL=https://your-domain.com:5000
```

### Security Notes
- Never commit API keys to Git
- Use strong SECRET_KEY for JWT
- Enable HTTPS in production
- Consider using MongoDB for better scalability
- Set up database backups

---

## Database Options

### SQLite (Default)
- File-based, good for small deployments
- Data persists in `project/backend/data/`

### MongoDB (Recommended for Production)
Update `.env`:
```bash
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=intrusive_thought_tracker_prod
```

---

## Monitoring and Maintenance

### Health Checks
- Backend: `GET /` returns status
- Frontend: Check if it loads properly

### Logs
- Docker: `docker-compose logs -f`
- PM2: `pm2 logs`
- Cloud: Check platform dashboards

### Backups
- SQLite: Backup `data/*.db` files
- MongoDB: Use mongodump or cloud provider backups

---

## Troubleshooting

### Common Issues
1. **CORS Errors**: Update `FRONTEND_URL` in backend
2. **API Key Issues**: Verify OpenRouter key is valid
3. **Database Issues**: Check file permissions or MongoDB connection
4. **Port Conflicts**: Ensure ports 3000 and 5000 are available

### Performance Tips
- Use Redis for session storage in production
- Enable gzip compression on Nginx
- Consider CDN for static assets
- Monitor OpenRouter API usage

---

## Domain and SSL

### SSL Certificate
```bash
# Let's Encrypt with Nginx
sudo certbot --nginx -d your-domain.com
```

### DNS Configuration
- A record: `@` -> your server IP
- A record: `api` -> your server IP (optional)

Choose the deployment option that best fits your needs and technical expertise!
