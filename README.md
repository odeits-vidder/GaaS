# GaaS

```Shell
docker build -t gaas:latest . && docker run -d -p 5000:5000 gaas;
curl -v --form "fileupload=@example.gv" http://localhost:5000/
```
