FROM node:23

WORKDIR /app

# Copy package.json first
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy everything else
COPY . .

# Expose the default Vite dev server port
EXPOSE 5173

# Start the Svelte app in dev mode
CMD ["npm", "run", "dev", "--", "--host"]
