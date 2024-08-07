from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from packages.retrieval_agent_fireworks.chain import agent_executor as retrieval_agent_fireworks_chain

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


add_routes(app, retrieval_agent_fireworks_chain, path="/retrieval-agent-fireworks")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
