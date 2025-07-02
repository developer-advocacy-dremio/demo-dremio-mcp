# 🧪 Running the Dremio MCP Client with PAT Fetcher via Docker Compose

Follow these steps to get up and running with a local Dremio instance, generate a Personal Access Token (PAT), and launch the MCP client with a web UI.

---

## ✅ Step 1: Start the Dremio Service

In your project directory (where `docker-compose.yml` is located), start only the Dremio container:

```bash
docker compose up -d dremio
```

This will start the Dremio service in the background.

## 🌐 Step 2: Create a Dremio User
Open your browser and go to:
```
http://localhost:9047
```

Follow the onboarding wizard to create a Dremio user.
For example, you can use:

```
Username: dremio

Password: dremio123
```

You’ll use these credentials in the next step to generate a PAT token.

## ⚙️ Step 3: Update pat-fetcher Environment Variables (if needed)
Make sure the environment variables under the pat-fetcher service in docker-compose.yml reflect the correct credentials you just created:

```yaml
environment:
  DREMIO_HOST: http://dremio:9047
  DREMIO_USERNAME: dremio
  DREMIO_PASSWORD: dremio123
```

Note: DREMIO_HOST must be http://dremio:9047 because the pat-fetcher runs on the same Docker network as dremio.

## 🔐 Step 4: Run the PAT Fetcher and Get Your Token
Now run the pat-fetcher container to log in and get your PAT token:

```bash
docker compose up --build pat-fetcher
```
In the logs, look for output like this:

```yaml
🎫 Your PAT Token:
abcd1234-ef56-gh78-ijkl-9012mnop3456
```

Copy this token — you’ll need it for the MCP client in the next step.

## 🔧 Step 5: Update MCP Client Environment Variables
In docker-compose.yml, update the DREMIO_PAT environment variable under the mcp-client service:

```yaml
environment:
  DREMIO_URI: http://dremio:9047
  DREMIO_PAT: abcd1234-ef56-gh78-ijkl-9012mnop3456
```

You can also review and edit the other LLM API keys and options in this block.

## 🚀 Step 6: Run the MCP Client with Web UI
Now launch the MCP client service:

```bash
docker compose up -d mcp-client
```

## 🌐 Step 7: Access the Web UI
Open your browser and visit:

```arduino
http://localhost:5000
```
You should now see your running MCP client web UI, ready to interact with Dremio and your connected LLMs!

## 🧹 Optional Cleanup
To stop all services:

```bash
docker compose down
```
To rebuild everything fresh:

```bash
docker compose up --build
```