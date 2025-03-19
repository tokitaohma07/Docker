# Use the official Nginx image as the base image
FROM nginx:latest

# Copy index.html to the Nginx HTML directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 to access the web page
EXPOSE 80

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]
