# Worker Service

Minimal Python worker used by the parent deployment-pipeline repository.

- `GET http://127.0.0.1:9090/health` returns HTTP 200 when healthy.
- The target Windows VM runs it through a pre-provisioned `AppWorker` Windows service.
- The service must invoke `C:\app-stack\worker\current\worker.py`.
