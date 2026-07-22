$root = $PSScriptRoot

Write-Host "Iniciando frontend y backend..." -ForegroundColor Cyan

Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$root\frontend'; npm run dev"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$root\backend'; python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

Write-Host "" 
Write-Host "Frontend: http://localhost:5173" -ForegroundColor Green
Write-Host "Backend docs: http://localhost:8000/docs" -ForegroundColor Green
Write-Host "Health check: http://localhost:8000/api/health" -ForegroundColor Green
