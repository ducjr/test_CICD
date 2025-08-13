# Django CI/CD Demo (GitHub Actions)

Dự án Django tối giản để minh hoạ CI/CD với GitHub Actions (YAML), có kèm Dockerfile để build/push image lên GitHub Container Registry (GHCR).

## Tính năng
- Django app đơn giản (`hello`) với 1 endpoint trả về `Hello, CI/CD!`.
- Test đơn giản dùng Django test runner.
- CI: chạy lint nhẹ (optional), migrate, test trên Ubuntu runner.
- CD: build và push Docker image lên GHCR khi push vào nhánh `main` (có thể tuỳ biến).

## Chạy local (Windows PowerShell)
```powershell
# Tạo venv
python -m venv .venv
. .\.venv\Scripts\Activate.ps1

# Cài dependencies
pip install -r requirements.txt

# Chạy migrate và test
python manage.py migrate --noinput
python manage.py test -v 2

# Chạy server dev
python manage.py runserver 0.0.0.0:8000
```

Mở http://127.0.0.1:8000/ để xem.

## CI/CD với GitHub Actions
1. Commit và push repo lên GitHub.
2. CI sẽ tự chạy trên push/pull request: cài deps, migrate, chạy test.
3. Khi push vào `main`, job CD sẽ build và push Docker image lên GHCR: `ghcr.io/<owner>/<repo>/django-cicd`.

### Yêu cầu quyền cho GHCR
- Vào Settings → Actions → General → Workflow permissions, bật “Read and write permissions”.
- Image sẽ được push với token mặc định `GITHUB_TOKEN` (đã cấu hình trong workflow).

## Build & chạy Docker local (tuỳ chọn)
```powershell
# Build image
docker build -t django-cicd:local .
# Chạy container
docker run --rm -p 8000:8000 -e DJANGO_SECRET_KEY=dev django-cicd:local
```

## Cấu trúc
- `cicd_demo/`: Django project
- `hello/`: Ứng dụng demo
- `.github/workflows/ci.yml`: Workflow CI/CD (YAML)
- `Dockerfile`: Build image chạy bằng Gunicorn
- `requirements.txt`: Dependencies

## Tuỳ biến tiếp theo
- Thêm flake8/black/isort.
- Thêm step deploy thực tế (Render, Fly.io, Azure, v.v.).
- Thêm database khác (PostgreSQL) và secrets tương ứng.
