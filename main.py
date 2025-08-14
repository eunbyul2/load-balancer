from fastapi import FastAPI, Request
import os
import socket

app = FastAPI(title="FastAPI Whoami")

@app.get("/")
async def read_root(request: Request):
  """
  호스트 및 수신 요청에 대한 정보를 반환합니다.
  """
  hostname = socket.gethostname()
  container_id = os.getenv("HOSTNAME", hostname)
  return {
    "hostname": container_id,
    "ip_address": request.client.host,
    "headers": dict(request.headers),
    "method": request.method,
    "path": request.url.path,
    "query_params": dict(request.query_params),
    "message": f"Hello from {container_id}!"
  }

@app.get("/health")
async def health_check():
  """간단한 헬스 체크 엔드포인트입니다."""
  return {"status": "ok"}