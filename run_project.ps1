$root = $PSScriptRoot
$venvPython = Join-Path $root "..\.venv\Scripts\python.exe"

function Stop-ProcessOnPort {
    param(
        [int]$Port
    )

    $connection = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($null -ne $connection) {
        $ownerPid = $connection.OwningProcess
        if ($ownerPid -gt 0) {
            Stop-Process -Id $ownerPid -Force -ErrorAction SilentlyContinue
            Write-Host "Puerto $Port liberado (PID $ownerPid)" -ForegroundColor Yellow
        }
    }
}

$backendPort = 8001

Write-Host "Iniciando frontend y backend..." -ForegroundColor Cyan
Stop-ProcessOnPort -Port 5173
Stop-ProcessOnPort -Port $backendPort

Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$root\frontend'; npm run dev"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$root\backend'; & '$venvPython' -m uvicorn app.main:app --host 0.0.0.0 --port $backendPort"

Write-Host "" 
Write-Host "Frontend: http://localhost:5173" -ForegroundColor Green
Write-Host "Backend docs: http://localhost:$backendPort/docs" -ForegroundColor Green
Write-Host "Health check: http://localhost:$backendPort/api/health" -ForegroundColor Green
