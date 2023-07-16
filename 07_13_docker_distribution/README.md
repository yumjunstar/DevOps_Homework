# 도커로 서비스 만들기

## 1. 계산기 서비스
실행
```
cd print_calculation_service
docker build -t calculation_service .
docker load -i calculation_docker.tar
docker run -it -v print_calculation_service/data:/app/data/ -v share_dir:/app/share_dir calculation_service:0.0.1
```
## 2. 웹 사이트 출력 서비스
```
cd print_web_service
docker build -t print_web_service .
docker load -i print_web_service.tar
docker run -it -p 5000:5000 -v share_dir:/app/share_dir --name print_web_service print_web_service:0.0.1
```