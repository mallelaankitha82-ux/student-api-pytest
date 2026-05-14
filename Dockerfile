# ---- Stage 1: Build React App ----
FROM node:20-alpine AS builder
WORKDIR /app

# package.json first copy cheste npm install cache aithundi
COPY package.json package-lock.json ./
RUN npm ci

COPY . .

# Build time lo backend URL pass cheyyali
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL

RUN npm run build

# ---- Stage 2: Serve with Nginx ----
FROM nginx:alpine
# Vite build output dist/ folder lo untundi
COPY --from=builder /app/dist /usr/share/nginx/html

# Optional: React Router ki nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]