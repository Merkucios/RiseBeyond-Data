

## 🗺️ Навигация по модулям



```csharp
Модуль 1  — Основы Computer Science
Модуль 2  — Основы сетей и протоколов
Модуль 3  — Основы System Design
Модуль 4  — Базы данных
Модуль 5  — Кэширование
Модуль 6  — Очереди и стриминг
Модуль 7  — Kubernetes и контейнеры
Модуль 8  — Мониторинг и наблюдаемость
Модуль 9  — Безопасность и PKI
Модуль 10 — Хранилища и резервное копирование
Модуль 11 — CI/CD и DevOps
Модуль 12 — Архитектурные паттерны
Модуль 13 — Game Backend (специфика)
Модуль 14 — Game Networking (специфика)
Модуль 15 — Game Analytics (специфика)
Модуль 16 — Game Economy & LiveOps (специфика)
Модуль 17 — Anti-Cheat системы (специфика)
Модуль 18 — Производительность и оптимизация
Модуль 19 — Железо и операционные системы
Модуль 20 — Карьера и система мышления
```

---

### Уровни сложности



```csharp
[B] — Beginner     → Читать, понять концепцию
[I] — Intermediate → Практика на тестовом стенде
[A] — Advanced     → Применять в реальных задачах
[E] — Expert       → Проектировать самостоятельно
```

---

## 📘 МОДУЛЬ 1 — Основы Computer Science



```csharp
1.   [B] [CS]  Как работает память: Stack vs Heap
2.   [B] [CS]  Типы данных: числа, строки, булевы — представление в памяти
3.   [B] [CS]  Массивы vs связные списки: когда что использовать
4.   [B] [CS]  Hash Map: внутреннее устройство, коллизии, load factor
5.   [B] [CS]  Очереди и стеки: структуры данных и применение
6.   [B] [CS]  Дерево: BST, обходы, балансировка
7.   [B] [CS]  Big O нотация: оценка сложности алгоритмов
8.   [B] [CS]  Процессы vs потоки: в чём разница
9.   [B] [CS]  Синхронный vs асинхронный код: блокирующий ввод-вывод
10.  [B] [CS]  Что происходит когда ты открываешь игру: от клика до рендера
11.  [I] [CS]  Конкурентность vs параллелизм: race conditions, deadlocks
12.  [I] [CS]  Event Loop: как работает асинхронность в Node.js / Go
13.  [I] [CS]  Сериализация: JSON, Protobuf, MessagePack — сравнение
14.  [I] [CS]  Битовые операции: флаги, маски — применение в играх
15.  [I] [CS]  Сортировка: Quick, Merge, Heap — когда что выбирать
16.  [I] [CS]  Хэш-функции: MD5, SHA, xxHash — применение в играх
17.  [I] [CS]  UUID vs ULID vs Snowflake ID: генерация ID в распределённых системах
18.  [A] [CS]  Lock-free структуры данных: CAS операции
19.  [A] [CS]  Memory-mapped файлы: быстрое чтение игровых ассетов
20.  [A] [CS]  SIMD инструкции: векторные вычисления для физики/графики
21.  [E] [CS]  Cache-oblivious алгоритмы: оптимизация под CPU cache
22.  [E] [CS]  Детерминированные алгоритмы: почему важно для мультиплеера
```

---

## 🌐 МОДУЛЬ 2 — Основы сетей и протоколов



```csharp
23.  [B] [NET]  Модель OSI: 7 уровней — что происходит с пакетом
24.  [B] [NET]  IP адресация: IPv4, IPv6, подсети, маски
25.  [B] [NET]  TCP: handshake, надёжность, flow control, congestion control
26.  [B] [NET]  UDP: почему без гарантий, но быстрее — критично для игр
27.  [B] [NET]  DNS: как разрешается имя в IP адрес
28.  [B] [NET]  HTTP/1.1: методы, заголовки, статус коды
29.  [B] [NET]  HTTP/2: мультиплексирование, server push, HPACK
30.  [B] [NET]  HTTP/3 / QUIC: UDP-based, 0-RTT, почему важно для игр
31.  [B] [NET]  TLS/SSL: handshake, сертификаты, HTTPS
32.  [I] [NET]  WebSocket: полнодуплексное соединение, framing протокол
33.  [I] [NET]  WebRTC: P2P для игр, ICE, STUN, TURN серверы
34.  [I] [NET]  NAT Traversal: как работает пробой NAT в P2P играх
35.  [I] [NET]  Firewall и порты: что блокируется, как обходить для игр
36.  [I] [NET]  Reverse Proxy: Nginx — маршрутизация, терминация TLS
37.  [I] [NET]  Load Balancing: Round Robin, Least Connections, IP Hash
38.  [I] [NET]  L4 vs L7 Load Balancing: в чём разница и когда что
39.  [I] [NET]  CDN: edge caching, как ускорить раздачу патчей/ассетов
40.  [I] [NET]  gRPC: Protocol Buffers, streaming, применение в игровом backend
41.  [I] [NET]  REST API: best practices, versioning, idempotency
42.  [A] [NET]  TCP Nagle Algorithm: отключение для игровых серверов
43.  [A] [NET]  Bandwidth estimation: адаптация качества под соединение
44.  [A] [NET]  Network simulation: тестирование с packet loss и latency
45.  [A] [NET]  BGP Anycast: глобальный роутинг для минимального пинга
46.  [A] [NET]  VLAN и сегментация: изоляция игровых серверов
47.  [A] [NET]  eBPF: перехват и анализ сетевого трафика
48.  [A] [NET]  DDoS: типы атак на игровые серверы и митигация
49.  [E] [NET]  DPDK: kernel bypass для ультранизкой латентности
50.  [E] [NET]  Kernel network tuning: sysctl параметры для игровых серверов
51.  [E] [NET]  Custom reliable UDP протокол: ENET, KCP, RUDP
52.  [E] [NET]  Проектирование сети дата-центра для игровой компании
```

---

## 🏗️ МОДУЛЬ 3 — Основы System Design



```csharp
53.  [B] [SD]  Что такое System Design и как думать архитектурно
54.  [B] [SD]  Вертикальное vs горизонтальное масштабирование
55.  [B] [SD]  Stateful vs Stateless сервисы: критично для игровых серверов
56.  [B] [SD]  CAP теорема: Consistency, Availability, Partition Tolerance
57.  [B] [SD]  BASE vs ACID: компромиссы в распределённых системах
58.  [B] [SD]  SLA, SLO, SLI: определения и применение в играх
59.  [B] [SD]  Latency vs Throughput: почему оба важны по-разному
60.  [B] [SD]  Single Point of Failure: как его найти и устранить
61.  [I] [SD]  PACELC теорема: расширение CAP для реальных систем
62.  [I] [SD]  Монолит vs Микросервисы: когда что выбирать для игры
63.  [I] [SD]  API Gateway паттерн: единая точка входа
64.  [I] [SD]  Идемпотентность: почему критично для игровых транзакций
65.  [I] [SD]  Back-of-the-envelope расчёты: оценка нагрузки для игры
66.  [I] [SD]  Проектирование под 1M / 10M / 100M игроков: разница подходов
67.  [I] [SD]  Паттерн CQRS: разделение чтения и записи
68.  [I] [SD]  Паттерн Event Sourcing: история событий как источник истины
69.  [I] [SD]  Паттерн Saga: распределённые транзакции в играх
70.  [A] [SD]  Паттерн Outbox: надёжная запись игровых событий
71.  [A] [SD]  Паттерн Bulkhead: изоляция отказов между сервисами
72.  [A] [SD]  Паттерн Circuit Breaker: устойчивость при каскадных падениях
73.  [A] [SD]  Паттерн Sidecar: вспомогательные процессы
74.  [A] [SD]  Two-Phase Commit: проблемы и почему избегают в играх
75.  [A] [SD]  Distributed Locking: Redis SETNX, Redlock алгоритм
76.  [A] [SD]  Consistent Hashing: алгоритм для шардинга игровых данных
77.  [A] [SD]  Gossip протокол: обнаружение нод в кластере
78.  [E] [SD]  Designing for Failure: Chaos Engineering для игровых систем
79.  [E] [SD]  Cell-based Architecture: изоляция регионов и серверов
80.  [E] [SD]  Multi-region Active-Active: глобальная игра без единого ЦОД
81.  [E] [SD]  Проектирование системы с нуля: полный цикл для онлайн-игры
```

---

## 💾 МОДУЛЬ 4 — Базы данных



```csharp
81.  [B] [DB]  Реляционные vs NoSQL: когда что выбирать для игры
82.  [B] [DB]  ACID: Atomicity, Consistency, Isolation, Durability
83.  [B] [DB]  Индексы: что это и почему ускоряет запросы
84.  [B] [DB]  Primary Key vs Foreign Key vs Composite Key
85.  [B] [DB]  SQL основы: SELECT, JOIN, GROUP BY, агрегации
86.  [I] [DB]  PostgreSQL: архитектура, MVCC, WAL журнал
87.  [I] [DB]  PostgreSQL: типы индексов B-Tree, Hash, GIN, GiST, BRIN
88.  [I] [DB]  PostgreSQL: EXPLAIN ANALYZE — чтение плана запроса
89.  [I] [DB]  PostgreSQL: партиционирование таблиц по времени
90.  [I] [DB]  Master/Replica: потоковая репликация PostgreSQL
91.  [I] [DB]  Синхронная vs асинхронная репликация: компромиссы
92.  [I] [DB]  Read Replicas: паттерны чтения, задержка репликации
93.  [I] [DB]  Connection Pooling: PgBouncer — зачем и как настроить
94.  [I] [DB]  Шардинг: горизонтальное партиционирование игровых данных
95.  [I] [DB]  Шардинг стратегии: Hash, Range, Directory для игровых сущностей
96.  [I] [DB]  Redis: структуры данных — String, Hash, List, Set, ZSet
97.  [I] [DB]  Redis: персистентность — RDB снимки vs AOF журнал
98.  [I] [DB]  Redis: Pub/Sub для игровых уведомлений
99.  [I] [DB]  Redis: Sorted Set для leaderboard — O(log N) операции
100. [I] [DB]  MongoDB: document model, агрегации, индексы
101. [A] [DB]  Patroni: автоматический failover PostgreSQL через etcd
102. [A] [DB]  Citus: распределённый PostgreSQL для шардинга
103. [A] [DB]  Redis Cluster: hash slots, resharding, failover
104. [A] [DB]  Redis Sentinel: мониторинг и автофейловер одного инстанса
105. [A] [DB]  ClickHouse: MergeTree engine, партиционирование, TTL
106. [A] [DB]  ClickHouse: репликация через ClickHouse Keeper
107. [A] [DB]  ClickHouse: материализованные представления для аналитики
108. [A] [DB]  Elasticsearch: инвертированный индекс, маппинги, шарды
109. [A] [DB]  Apache Druid: real-time OLAP, ingestion из Kafka
110. [A] [DB]  Cassandra: wide-column, consistent hashing, запись без блокировок
111. [A] [DB]  TimescaleDB: time-series расширение для PostgreSQL
112. [E] [DB]  Polyglot Persistence: несколько БД в одной игровой системе
113. [E] [DB]  Database per Service: паттерн для независимых микросервисов
114. [E] [DB]  Проектирование схемы для 100M игровых профилей
115. [E] [DB]  Hot/Warm/Cold данные: тиерирование игровых данных
116. [E] [DB]  Zero-downtime миграции схемы БД в production
```

---

## ⚡ МОДУЛЬ 5 — Кэширование



```csharp
117. [B] [CACHE]  Что такое кэш и зачем он нужен
118. [B] [CACHE]  Cache Hit vs Cache Miss: метрики эффективности
119. [B] [CACHE]  TTL: время жизни записи в кэше
120. [B] [CACHE]  Cache Eviction политики: LRU, LFU, FIFO, Random
121. [I] [CACHE]  Cache-Aside паттерн: приложение сначала идёт в кэш
122. [I] [CACHE]  Write-Through паттерн: запись одновременно в кэш и БД
123. [I] [CACHE]  Write-Back паттерн: запись в БД отложено
124. [I] [CACHE]  Read-Through паттерн: кэш сам идёт в БД при промахе
125. [I] [CACHE]  Redis как кэш: настройка maxmemory и eviction policy
126. [I] [CACHE]  Кэширование игровых профилей: стратегия и инвалидация
127. [I] [CACHE]  CDN кэширование: игровые ассеты, патчи, статика
128. [A] [CACHE]  Cache Stampede: проблема и probabilistic early expiration
129. [A] [CACHE]  Thundering Herd: что это и как защититься
130. [A] [CACHE]  Cache Invalidation: самая сложная проблема в кэшировании
131. [A] [CACHE]  Distributed Cache: консистентность между нодами
132. [A] [CACHE]  Local Cache + Distributed Cache: многоуровневое кэширование
133. [A] [CACHE]  Кэширование результатов матчмейкинга
134. [E] [CACHE]  Кэш для игрового состояния: write-back к БД
135. [E] [CACHE]  Проектирование кэш-слоя для 1M одновременных игроков
```

---

## 📨 МОДУЛЬ 6 — Очереди и стриминг



```csharp
136. [B] [MSG]  Message Queue: зачем нужна асинхронность
137. [B] [MSG]  Producer / Consumer паттерн
138. [B] [MSG]  At-most-once, At-least-once, Exactly-once: гарантии доставки
139. [B] [MSG]  Queue vs Topic: в чём разница
140. [I] [MSG]  Apache Kafka: архитектура — broker, topic, partition, offset
141. [I] [MSG]  Kafka: Consumer Groups — параллельная обработка
142. [I] [MSG]  Kafka: репликация, ISR, acks=all для надёжности
143. [I] [MSG]  Kafka: retention политики, compacted topics
144. [I] [MSG]  Kafka: игровые события — kill, match_start, purchase
145. [I] [MSG]  Kafka Connect: CDC из PostgreSQL через Debezium
146. [I] [MSG]  RabbitMQ: exchanges, queues, bindings, DLQ
147. [I] [MSG]  RabbitMQ vs Kafka: когда что использовать
148. [A] [MSG]  Kafka Streams: stateful обработка без отдельного кластера
149. [A] [MSG]  Apache Flink: DataStream API, операторы трансформации
150. [A] [MSG]  Flink: Window операции — Tumbling, Sliding, Session
151. [A] [MSG]  Flink: State Management, RocksDB backend
152. [A] [MSG]  Flink: Watermarks — обработка out-of-order событий
153. [A] [MSG]  Flink: Exactly-once через checkpointing
154. [A] [MSG]  Backpressure: проблема и механизмы управления потоком
155. [A] [MSG]  Kafka KRaft: отказ от ZooKeeper, новая архитектура
156. [E] [MSG]  Lambda Architecture: batch + speed layer
157. [E] [MSG]  Kappa Architecture: только стриминг
158. [E] [MSG]  Проектирование event pipeline для 2M событий в минуту
159. [E] [MSG]  Exactly-once в распределённых игровых системах
```

---

## ☸️ МОДУЛЬ 7 — Kubernetes и контейнеры



```csharp
160. [B] [K8S]  Docker: образы, слои, Dockerfile — базовое понимание
161. [B] [K8S]  Docker: volumes, networks, docker-compose
162. [B] [K8S]  Kubernetes: зачем нужен оркестратор
163. [B] [K8S]  Kubernetes: Pod, Deployment, Service — базовые объекты
164. [B] [K8S]  Kubernetes: Namespace, Label, Selector
165. [B] [K8S]  Kubernetes: ConfigMap и Secret
166. [I] [K8S]  Kubernetes: Ingress и Ingress Controller (Nginx)
167. [I] [K8S]  Kubernetes: PersistentVolume, PVC, StorageClass
168. [I] [K8S]  Kubernetes: HPA — автоскейлинг по CPU/RAM/метрикам
169. [I] [K8S]  Kubernetes: StatefulSet для баз данных
170. [I] [K8S]  Kubernetes: DaemonSet, Job, CronJob
171. [I] [K8S]  Kubernetes: Resource Requests/Limits, QoS классы
172. [I] [K8S]  Kubernetes: liveness, readiness, startup probes
173. [I] [K8S]  Helm: charts, values, templates, hooks, rollback
174. [I] [K8S]  Kubernetes: NetworkPolicy — изоляция трафика
175. [A] [K8S]  Kubernetes: RBAC — роли, привязки, ServiceAccount
176. [A] [K8S]  Kubernetes: Admission Controllers и Webhooks
177. [A] [K8S]  Kubernetes: CRD и Operators — расширение API
178. [A] [K8S]  Kubernetes: etcd — роль, бэкап, восстановление
179. [A] [K8S]  Kubernetes: Scheduler — affinity, taints, tolerations
180. [A] [K8S]  Kubernetes: VPA вертикальный автоскейлинг
181. [A] [K8S]  ArgoCD: GitOps, App of Apps паттерн
182. [A] [K8S]  Cilium: eBPF networking, Network Policy
183. [A] [K8S]  Agones: управление игровыми серверами в Kubernetes
184. [A] [K8S]  Agones: GameServer, Fleet, GameServerAllocation
185. [A] [K8S]  Agones: автоскейлинг флота игровых серверов
186. [A] [K8S]  Istio: Service Mesh, mTLS, circuit breaker, canary
187. [E] [K8S]  Kubernetes: multi-cluster federation
188. [E] [K8S]  Kubernetes: capacity planning и bin packing
189. [E] [K8S]  Kubernetes: upgrade стратегии без downtime
190. [E] [K8S]  Проектирование K8s кластера для игровой компании
```

---

## 📈 МОДУЛЬ 8 — Мониторинг и наблюдаемость



```csharp
191. [B] [OBS]  Три столпа наблюдаемости: Metrics, Logs, Traces
192. [B] [OBS]  RED метод: Rate, Errors, Duration — для игровых API
193. [B] [OBS]  USE метод: Utilization, Saturation, Errors — для серверов
194. [B] [OBS]  Метрики игровых серверов: CCU, TPS, latency, tick rate
195. [I] [OBS]  Prometheus: архитектура, scrape, exporters
196. [I] [OBS]  PromQL: базовые запросы, rate(), histogram_quantile()
197. [I] [OBS]  Grafana: дашборды, переменные, annotations, alerts
198. [I] [OBS]  Alertmanager: routes, receivers, inhibitions, silences
199. [I] [OBS]  Node Exporter: метрики с хостов — CPU, RAM, Disk, Net
200. [I] [OBS]  kube-state-metrics: состояние K8s объектов
201. [I] [OBS]  ELK Stack: Elasticsearch + Logstash + Kibana
202. [I] [OBS]  Filebeat: сбор логов с контейнеров и хостов
203. [I] [OBS]  Fluent Bit: лёгкий log shipper для K8s
204. [I] [OBS]  Zabbix: агенты, шаблоны, триггеры для legacy инфры
205. [A] [OBS]  Grafana Loki: LogQL, label-based indexing
206. [A] [OBS]  Thanos / Mimir: долгосрочное хранение метрик
207. [A] [OBS]  Distributed Tracing: spans, trace con propagation
208. [A] [OBS]  Jaeger: трейсинг запросов через микросервисы игры
209. [A] [OBS]  OpenTelemetry: стандарт инструментирования
210. [A] [OBS]  Grafana Tempo: хранение трейсов
211. [A] [OBS]  SLO-based alerting: Error Budget подход
212. [A] [OBS]  Игровые алерты: tick rate drop, matchmaking timeout
213. [A] [OBS]  Мониторинг Kafka: consumer lag, partition offsets
214. [E] [OBS]  Observability-driven Development в игровых командах
215. [E] [OBS]  Capacity Planning по историческим метрикам игры
216. [E] [OBS]  Корреляция метрик, логов и трейсов в одном событии
```

---

## 🔐 МОДУЛЬ 9 — Безопасность и PKI



```csharp
217. [B] [SEC]  PKI: Certificate Authority, chain of trust, сертификаты
218. [B] [SEC]  X.509 сертификаты: структура, поля, срок действия
219. [B] [SEC]  TLS mTLS: взаимная аутентификация сервисов
220. [B] [SEC]  SSH: key-based auth, authorized_keys, known_hosts
221. [B] [SEC]  Аутентификация vs Авторизация: разница
222. [B] [SEC]  OAuth2 / OpenID Connect: flows для игровых аккаунтов
223. [I] [SEC]  JWT токены: структура, подпись, валидация, refresh
224. [I] [SEC]  Session Management: cookie vs token для игровых клиентов
225. [I] [SEC]  HashiCorp Vault: архитектура, seal/unseal, auth methods
226. [I] [SEC]  Vault: Dynamic Secrets для PostgreSQL
227. [I] [SEC]  Vault: PKI Secrets Engine — внутренний CA
228. [I] [SEC]  cert-manager: ClusterIssuer, Certificate, ACME protocol
229. [I] [SEC]  SSH-CA через Vault: краткосрочные SSH сертификаты
230. [I] [SEC]  Self-hosted CA: Step CA — установка и выпуск сертификатов
231. [I] [SEC]  Keycloak: SSO, OAuth2/OIDC, RBAC для игровой платформы
232. [A] [SEC]  Vault: AppRole и Kubernetes Auth Method
233. [A] [SEC]  Vault: Transit Encryption — шифрование данных игроков
234. [A] [SEC]  OPA / Gatekeeper: Policy as Code в Kubernetes
235. [A] [SEC]  Falco: runtime security, аномалии в контейнерах
236. [A] [SEC]  Trivy: сканирование образов на уязвимости
237. [A] [SEC]  Teleport: Zero Trust доступ к серверам и K8s
238. [A] [SEC]  Rate Limiting для защиты игрового API
239. [A] [SEC]  DDoS митигация: Cloudflare, anycast, игровые серверы
240. [A] [SEC]  Secrets rotation: автоматическая без downtime
241. [E] [SEC]  Zero Trust Network Architecture для игровой инфры
242. [E] [SEC]  PCI DSS требования: платёжная система в игре
243. [E] [SEC]  Supply Chain Security: SBOM, Cosign, Sigstore
244. [E] [SEC]  Penetration Testing игрового backend
```

---

## 💿 МОДУЛЬ 10 — Хранилища и резервное копирование



```csharp
245. [B] [STR]  Block vs File vs Object Storage: разница и применение
246. [B] [STR]  RAID уровни: 0, 1, 5, 6, 10 — когда что выбирать
247. [B] [STR]  HDD vs SSD vs NVMe: характеристики, IOPS, latency
248. [I] [STR]  MinIO: S3-compatible, erasure coding, bucket policies
249. [I] [STR]  Резервное копирование PostgreSQL: pg_dump, pg_basebackup
250. [I] [STR]  WAL archiving: Point-in-Time Recovery для игровых БД
251. [I] [STR]  Backup стратегия: правило 3-2-1 для игровых данных
252. [A] [STR]  Ceph: архитектура RADOS, OSD, Monitor, CRUSH алгоритм
253. [A] [STR]  Longhorn: distributed block storage в Kubernetes
254. [A] [STR]  S3 для игровых ассетов: versioning, lifecycle policies
255. [A] [STR]  Репликация данных между регионами: игровые бэкапы
256. [E] [STR]  Tiered Storage: hot/warm/cold для игровых данных
257. [E] [STR]  Data Lifecycle Management: TTL политики для логов/событий
258. [E] [STR]  Disaster Recovery план для игрового сервиса
```

---

## 🔄 МОДУЛЬ 11 — CI/CD и DevOps



```csharp
259. [B] [CICD]  Git: ветки, merge, rebase, конфликты
260. [B] [CICD]  Git Flow vs Trunk-Based Development
261. [B] [CICD]  Что такое CI/CD: концепция автоматизации
262. [B] [CICD]  GitLab CI: stages, jobs, artifacts, кэширование
263. [I] [CICD]  Docker multi-stage builds: оптимизация образов
264. [I] [CICD]  Semantic Versioning: major.minor.patch и changelog
265. [I] [CICD]  GitOps: принципы, Git как источник истины
266. [I] [CICD]  ArgoCD: App of Apps, синхронизация, rollback
267. [I] [CICD]  Harbor: приватный registry, сканирование образов
268. [I] [CICD]  Terraform: IaC основы, state, plan, apply
269. [I] [CICD]  Ansible: playbooks, роли, inventory
270. [A] [CICD]  Canary Deployments: постепенный роллаут для игры
271. [A] [CICD]  Blue/Green Deployment: переключение без downtime
272. [A] [CICD]  Feature Flags: A/B тесты игровых механик
273. [A] [CICD]  Hotfix процесс: быстрый патч в production
274. [A] [CICD]  Database migrations в CI/CD: Flyway, Liquibase
275. [A] [CICD]  SonarQube: статический анализ кода
276. [E] [CICD]  Progressive Delivery: автоматический rollback по метрикам
277. [E] [CICD]  Platform Engineering: Internal Developer Platform
278. [E] [CICD]  Проектирование CI/CD для 50 микросервисов игры
```

---

## 🏛️ МОДУЛЬ 12 — Архитектурные паттерны



```csharp
279. [B] [ARCH]  Монолит: плюсы, минусы, когда оправдан для игры
280. [B] [ARCH]  Микросервисы: разложение по доменам игры
281. [B] [ARCH]  Domain-Driven Design: ubiquitous language, bounded cons
282. [B] [ARCH]  Синхронная vs асинхронная коммуникация
283. [I] [ARCH]  API Design: REST best practices для игрового backend
284. [I] [ARCH]  Strangler Fig: постепенная миграция с монолита
285. [I] [ARCH]  Database per Service: независимость микросервисов
286. [I] [ARCH]  Паттерн Outbox: надёжная отправка событий в Kafka
287. [I] [ARCH]  Паттерн Saga Choreography: события без оркестратора
288. [I] [ARCH]  Паттерн Saga Orchestration: центральный координатор
289. [A] [ARCH]  CQRS: разделение команд и запросов в игровых сервисах
290. [A] [ARCH]  Event Sourcing: история матча как последовательность событий
291. [A] [ARCH]  Idempotency Keys: защита от дублирования покупок
292. [A] [ARCH]  Rate Limiting паттерны: Token Bucket, Leaky Bucket
293. [A] [ARCH]  Retry с Exponential Backoff и Jitter
294. [A] [ARCH]  Timeout, Retry, Circuit Breaker: resilience триада
295. [E] [ARCH]  Data Mesh: децентрализованное управление данными
296. [E] [ARCH]  Event-Driven Architecture: полная игровая система
297. [E] [ARCH]  Multi-Region Active-Active: глобальная игровая платформа
298. [E] [ARCH]  Проектирование backend для 10M DAU игры
```

---

## 🎮 МОДУЛЬ 13 — Game Backend (специфика)



```csharp
299. [B] [GB]   Архитектура онлайн-игры: все компоненты и связи
300. [B] [GB]   Типы игровых серверов: Dedicated vs P2P vs Listen Server
301. [B] [GB]   CCU (Concurrent Users): как считать и планировать мощности
302. [B] [GB]   Game Session: жизненный цикл от создания до завершения
303. [B] [GB]   Player Profile: что хранить и как структурировать
304. [B] [GB]   Authentication для игр: email, Steam, Google, Apple
305. [I] [GB]   Session Token: выпуск, валидация, refresh, отзыв
306. [I] [GB]   Matchmaking: базовые алгоритмы подбора игроков
307. [I] [GB]   ELO система: расчёт рейтинга, K-фактор
308. [I] [GB]   Glicko-2: продвинутый рейтинг с учётом неопределённости
309. [I] [GB]   Lobby Service: создание, ожидание, старт матча
310. [I] [GB]   Game Server Allocation: выдача сервера под матч
311. [I] [GB]   Inventory System: предметы, стаки, трансферы
312. [I] [GB]   Friend System: список друзей, онлайн статус
313. [I] [GB]   Chat Service: глобальный, командный, приватный чат
314. [I] [GB]   Notification Service: push, in-game, email уведомления
315. [I] [GB]   Leaderboard: глобальный, региональный, друзья
316. [A] [GB]   Skill-based Matchmaking (SBMM): алгоритмы и баланс
317. [A] [GB]   Latency-based Matchmaking: выбор сервера по пингу
318. [A] [GB]   Matchmaking Queue: приоритеты, таймауты, группы
319. [A] [GB]   Agones: Fleet, GameServer, Allocation API
320. [A] [GB]   Game Server Lifecycle в Agones: Ready → Allocated → Shutdown
321. [A] [GB]   Autoscaling Fleet: Buffer-based scaling в Agones
322. [A] [GB]   Игровой Replay: хранение и воспроизведение матчей
323. [A] [GB]   Spectator System: наблюдение за матчем в реальном времени
324. [A] [GB]   Reconnect механизм: восстановление после разрыва соединения
325. [A] [GB]   Tournament System: сетки, раунды, автоматизация
326. [A] [GB]   Season System: Battle Pass, прогрессия, сброс рейтинга
327. [E] [GB]   Проектирование Matchmaking для 500K одновременных игроков
328. [E] [GB]   Cross-platform аккаунты: PC + Console + Mobile
329. [E] [GB]   Server-side Game Logic: авторитетный сервер
330. [E] [GB]   Проектирование полного backend для MMORPG
```

---

## 🌐 МОДУЛЬ 14 — Game Networking (специфика)



```csharp
331. [B] [GN]   Почему UDP а не TCP для игр: latency vs reliability
332. [B] [GN]   Понятие tick rate: 20/60/128 tick серверы
333. [B] [GN]   Пинг, джиттер, потеря пакетов: влияние на геймплей
334. [B] [GN]   Interpolation: сглаживание движения между тиками
335. [B] [GN]   Extrapolation / Dead Reckoning: предсказание позиции
336. [I] [GN]   Client-side Prediction: локальное применение ввода
337. [I] [GN]   Server Reconciliation: согласование клиента с сервером
338. [I] [GN]   Lag Compensation: перемотка состояния для hit detection
339. [I] [GN]   Snapshot Interpolation: Gabriel Gambetta метод
340. [I] [GN]   Delta Compression: отправка только изменений состояния
341. [I] [GN]   Area of Interest (AOI): отправка только видимых объектов
342. [I] [GN]   WebSocket для игр: framing, heartbeat, reconnect
343. [I] [GN]   WebRTC Data Channel: P2P для браузерных игр
344. [I] [GN]   NAT Traversal: STUN, TURN, ICE для P2P соединений
345. [A] [GN]   Reliable UDP: ENET, KCP, LiteNetLib алгоритмы
346. [A] [GN]   Packet Priority и bandwidth budget
347. [A] [GN]   Congestion Control для игровых протоколов
348. [A] [GN]   Детерминированный Lockstep: стратегии и файтинги
349. [A] [GN]   Rollback Netcode (GGPO): мгновенный отклик + откат
350. [A] [GN]   State Synchronization vs Event Synchronization
351. [A] [GN]   Zoning в MMORPG: разбивка мира на зоны/инстансы
352. [A] [GN]   Interest Management: пространственное хэширование
353. [E] [GN]   Масштабирование до 1000 игроков в одной локации
354. [E] [GN]   Network simulation: тестирование при плохом соединении
355. [E] [GN]   Кастомный игровой протокол поверх UDP с нуля
356. [E] [GN]   Проектирование сетевой архитектуры Battle Royale
```

---

## 📊 МОДУЛЬ 15 — Game Analytics (специфика)



```csharp
357. [B] [GA]   Зачем аналитика в играх: примеры влияния на дизайн
358. [B] [GA]   Ключевые игровые метрики: DAU, MAU, ARPU, ARPPU
359. [B] [GA]   Retention: D1, D7, D30 — что считать нормой
360. [B] [GA]   Funnel анализ: от установки до первой покупки
361. [B] [GA]   Session Length: длина сессии и её влияние
362. [I] [GA]   Event-based аналитика: схема событий для игры
363. [I] [GA]   ClickHouse: быстрые агрегации по игровым событиям
364. [I] [GA]   Grafana: игровые дашборды — CCU, revenue, errors
365. [I] [GA]   Kafka → ClickHouse pipeline: real-time аналитика
366. [I] [GA]   Player Segmentation: новички, хардкор, киты, whales
367. [I] [GA]   Churn Prediction: кто уйдёт из игры
368. [I] [GA]   A/B тестирование: статистическая значимость результатов
369. [A] [GA]   Apache Flink для игровой аналитики в реальном времени
370. [A] [GA]   Cohort Analysis: поведение групп игроков по времени
371. [A] [GA]   Heat Maps: анализ перемещения игроков по карте
372. [A] [GA]   Anomaly Detection: автоматическое выявление читеров
373. [A] [GA]   Player Lifetime Value (LTV): расчёт и прогнозирование
374. [A] [GA]   Data Pipeline: Kafka → Flink → ClickHouse → Grafana
375. [A] [GA]   Game Balance Analytics: анализ win rate оружий/классов
376. [E] [GA]   Real-time Dashboard для 1M событий в секунду
377. [E] [GA]   ML Pipeline для предсказания поведения игроков
378. [E] [GA]   Data Lake для игровой компании: архитектура
379. [E] [GA]   Проектирование аналитической системы с нуля
```

---

## 💰 МОДУЛЬ 16 — Game Economy и LiveOps (специфика)



```csharp
380. [B] [ECO]  Virtual Economy: soft currency vs hard currency
381. [B] [ECO]  Монетизация: IAP, Battle Pass, Loot Box, Subscription
382. [B] [ECO]  Inflation в игровой экономике: причины и последствия
383. [I] [ECO]  Transaction Integrity: атомарность покупок
384. [I] [ECO]  Idempotency в платежах: защита от двойных списаний
385. [I] [ECO]  Интеграция платёжных систем: App Store, Google Play, Stripe
386. [I] [ECO]  Webhook от платёжных систем: обработка событий
387. [I] [ECO]  Receipt Validation: проверка чеков App Store / Google Play
388. [I] [ECO]  Loot Box система: таблицы вероятностей, гарантированные дропы
389. [I] [ECO]  Battle Pass: прогрессия, XP, уровни, награды
390. [A] [ECO]  Anti-Fraud: выявление мошеннических транзакций
391. [A] [ECO]  Economy Balancing: sink и source механики валюты
392. [A] [ECO]  Dynamic Pricing: персонализированные предложения
393. [A] [ECO]  LiveOps Events: временные события, технический дизайн
394. [A] [ECO]  Remote Config: Firebase, LaunchDarkly для игровых параметров
395. [A] [ECO]  Feature Flags: плавный роллаут игровых фич
396. [A] [ECO]  Промокоды: генерация, валидация, one-time использование
397. [E] [ECO]  Проектирование устойчивой игровой экономики
398. [E] [ECO]  Compliance: GDPR, COPPA для игровых данных
399. [E] [ECO]  PCI DSS: требования к хранению платёжных данных
400. [E] [ECO]  Аудит лог транзакций: неизменяемая история
```

---

## 🛡️ МОДУЛЬ 17 — Anti-Cheat системы (специфика)



```csharp
401. [B] [AC]   Типы читов: aimbot, wallhack, speedhack, exploits
402. [B] [AC]   Client-side vs Server-side валидация
403. [B] [AC]   Авторитетный сервер: почему клиент не должен доверять
404. [I] [AC]   Server-side валидация действий: движение, стрельба
405. [I] [AC]   Санитизация входящих данных от клиента
406. [I] [AC]   Rate Limiting действий: защита от speedhack
407. [I] [AC]   Statistical Anomaly Detection: подозрительная точность
408. [I] [AC]   Replay Analysis: пост-матчевый анализ на читы
409. [A] [AC]   Behavioral Analysis: паттерны движения мыши
410. [A] [AC]   Machine Learning для детекции читеров
411. [A] [AC]   Flink: real-time анализ игровых событий на аномалии
412. [A] [AC]   Ban System: временные и перманентные блокировки
413. [A] [AC]   Hardware Fingerprinting: обход бана по железу
414. [A] [AC]   Shadow Ban: незаметная изоляция читеров
415. [E] [AC]   Trust Score система: репутация игрока
416. [E] [AC]   Проектирование Anti-Cheat системы для FPS
417. [E] [AC]   Kernel-level Anti-Cheat: принципы (EasyAntiCheat, BattlEye)
```

---

## ⚡ МОДУЛЬ 18 — Производительность и оптимизация



```csharp
418. [B] [PERF]  Что такое профилирование: CPU, Memory, IO, Network
419. [B] [PERF]  Bottleneck: как найти узкое место в системе
420. [B] [PERF]  Benchmarking: методология правильных измерений
421. [I] [PERF]  Load Testing: k6, Locust, JMeter для игрового backend
422. [I] [PERF]  PostgreSQL: медленные запросы, pg_stat_statements
423. [I] [PERF]  Connection Pool tuning: размер пула, таймауты
424. [I] [PERF]  Redis: memory optimization, объём данных
425. [I] [PERF]  Kafka: tuning throughput vs latency
426. [A] [PERF]  Flamegraph: профилирование CPU в production
427. [A] [PERF]  Linux perf: системное профилирование
428. [A] [PERF]  JVM tuning: GC pauses для Java игровых серверов
429. [A] [PERF]  Go runtime: goroutine profiling, pprof
430. [A] [PERF]  Network tuning: TCP/UDP параметры ядра Linux
431. [A] [PERF]  ClickHouse: оптимизация запросов, профилирование
432. [E] [PERF]  Capacity Planning: сколько серверов нужно для N игроков
433. [E] [PERF]  Stress Testing: поведение системы под экстремальной нагрузкой
434. [E] [PERF]  Chaos Engineering: намеренные отказы для проверки устойчивости
```

---

## 🖥️ МОДУЛЬ 19 — Железо и операционные системы



```csharp
435. [B] [HW]   CPU: cores, threads, clock speed, cache L1/L2/L3
436. [B] [HW]   RAM: DDR4 vs DDR5, ECC память, каналы
437. [B] [HW]   Disk: HDD vs SSD vs NVMe — IOPS, latency, throughput
438. [B] [HW]   Network: Ethernet, SFP+, скорости 1G/10G/25G/100G
439. [B] [HW]   Что такое IPMI / iDRAC: удалённое управление сервером
440. [I] [HW]   NUMA: Non-Uniform Memory Access, влияние на PostgreSQL
441. [I] [HW]   Linux: процессы, файловые дескрипторы, ulimits
442. [I] [HW]   Linux: sysctl параметры для игровых серверов
443. [I] [HW]   Linux: systemd — юниты, зависимости, логи
444. [I] [HW]   Linux: cgroups — ограничение ресурсов (основа K8s)
445. [I] [HW]   Linux: namespaces — изоляция (основа Docker)
446. [I] [HW]   Выбор железа: CPU vs RAM vs NVMe для разных нагрузок
447. [A] [HW]   NVMe: queue depth, io_uring, latency профиль
448. [A] [HW]   CPU pinning: изоляция ядер для latency-sensitive сервисов
449. [A] [HW]   Huge Pages: transparent vs explicit, применение
450. [A] [HW]   Network interrupt affinity: привязка прерываний к ядрам
451. [E] [HW]   Проектирование физической инфры для игровой компании
452. [E] [HW]   Datacenter выбор: colocation vs cloud для игры
453. [E] [HW]   Hybrid Cloud: on-premise + cloud burst для пиков
```

---

## 🧠 МОДУЛЬ 20 — Карьера и система мышления



```csharp
454. [B] [CAR]  Как читать техническую документацию эффективно
455. [B] [CAR]  Как строить тестовый стенд дома: минимальный набор
456. [B] [CAR]  Как подходить к изучению новых технологий
457. [I] [CAR]  Как проводить Design Review: что проверять
458. [I] [CAR]  Написание Architecture Decision Records (ADR)
459. [I] [CAR]  Runbook: документирование операционных процедур
460. [I] [CAR]  Post-Mortem: разбор инцидентов без поиска виноватых
461. [I] [CAR]  On-Call: дежурство и реакция на инциденты
462. [A] [CAR]  System Design Interview: как структурировать ответ
463. [A] [CAR]  Trade-off мышление: нет правильного ответа, есть компромиссы
464. [A] [CAR]  Как оценивать технический долг
465. [A] [CAR]  GameDev Backend Engineer: карьерный путь и стек
466. [E] [CAR]  Staff Engineer мышление: системный взгляд
467. [E] [CAR]  Как проектировать систему за 45 минут (интервью)
468. [E] [CAR]  Principal Engineer: влияние на техническое направление
```

---

## 📊 Итоговая статистика



```csharp
┌─────────────────────────────────────────┐
│           Всего тем: 468                │
├──────────────┬──────────────────────────┤
│  [B] Beginner     │  ~120 тем  (26%)   │
│  [I] Intermediate │  ~170 тем  (36%)   │
│  [A] Advanced     │  ~130 тем  (28%)   │
│  [E] Expert       │   ~48 тем  (10%)   │
├──────────────┴──────────────────────────┤
│         Модулей: 20                     │
│  Общие (SD): 12 модулей / 298 тем       │
│  GameDev специфика: 5 модулей / 119 тем │
│  Прочее: 3 модуля / 51 тема            │
└─────────────────────────────────────────┘
```

---

## 🗓️ Рекомендуемый план изучения



```csharp
Фаза 1 — Фундамент (3 месяца)
├── Модуль 1  [B] CS основы
├── Модуль 2  [B][I] Сети
├── Модуль 3  [B] SD основы
└── Модуль 13 [B] Game Backend концепции

Фаза 2 — Практика (4 месяца)
├── Модуль 4  [I] Базы данных + PostgreSQL + Redis
├── Модуль 5  [I] Кэширование
├── Модуль 6  [I] Kafka
├── Модуль 7  [I] Kubernetes + Helm + Agones
└── Модуль 14 [I] Game Networking

Фаза 3 — Углубление (4 месяца)
├── Модуль 8  [A] Мониторинг
├── Модуль 9  [A] Безопасность
├── Модуль 12 [A] Архитектурные паттерны
├── Модуль 13 [A] Game Backend продвинутое
└── Модуль 15 [I][A] Game Analytics

Фаза 4 — Экспертиза (5 месяцев)
├── Модуль 16 [A][E] Economy & LiveOps
├── Модуль 17 [A][E] Anti-Cheat
├── Модуль 18 [E] Производительность
├── Модуль 19 [A][E] Железо
└── Модуль 20 [E] Карьера и мышление
```