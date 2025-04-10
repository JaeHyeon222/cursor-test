# AI 이미지 생성 웹 애플리케이션

## 프로젝트 개요
이 프로젝트는 사용자가 입력한 프롬프트를 기반으로 OpenAI의 DALL-E 3를 활용하여 이미지를 생성하는 웹 애플리케이션입니다.

## 시스템 아키텍처

### Frontend 설계 원칙
1. **기술 스택**
   - HTML5: 웹 페이지 구조
   - CSS3: 스타일링
   - JavaScript: 동적 기능 구현
   - Fetch API: 백엔드 통신

2. **주요 기능**
   - 프롬프트 입력 폼
   - 이미지 표시
   - 로딩 상태 표시
   - 에러 처리

3. **구조**
   - 단일 HTML 파일
   - 인라인 CSS
   - 모듈화된 JavaScript

4. **UX/UI 원칙**
   - 반응형 디자인
   - 직관적인 사용자 인터페이스
   - 실시간 피드백
   - 접근성 고려

### Backend 설계 원칙
1. **기술 스택**
   - FastAPI: Python 웹 프레임워크
   - OpenAI API: 이미지 생성
   - Pydantic: 데이터 검증

2. **API 설계**
   - RESTful API 원칙 준수
   - 명확한 엔드포인트 구조
   - 적절한 HTTP 상태 코드 사용
   - API 문서화 (Swagger/OpenAPI)

3. **보안**
   - API 키 관리
   - CORS 설정
   - 입력 데이터 검증
   - 요청 제한 (Rate Limiting)

4. **에러 처리**
   - 구조화된 에러 응답
   - 로깅 시스템
   - 예외 처리 미들웨어

## 디렉토리 구조
```
project/
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       └── api.py
│   │   └── core/
│   │       └── config.py
│   ├── tests/
│   └── requirements.txt
├── .env
├── run.bat
└── README.md
```

## 개발 환경 설정
1. **필수 도구**
   - Python (v3.9 이상)
   - Git
   - 웹 브라우저 (Chrome, Firefox 등)

2. **환경 변수 설정**
   루트 디렉토리에 `.env` 파일을 생성하고 다음 내용을 추가:
   ```
   # 백엔드 설정
   OPENAI_API_KEY=your_api_key_here
   BACKEND_HOST=localhost
   BACKEND_PORT=8000

   # 프론트엔드 설정
   FRONTEND_HOST=localhost
   FRONTEND_PORT=3000
   ```

## 개발 가이드라인
1. **코드 스타일**
   - Black + isort (Backend)
   - Git 커밋 컨벤션 준수

2. **테스트**
   - Pytest (Backend)
   - 테스트 커버리지 80% 이상 유지

3. **CI/CD**
   - GitHub Actions
   - 자동화된 테스트
   - 코드 품질 검사

## 배포 전략
1. **개발 환경**
   - 로컬 개발 서버
   - Docker 컨테이너화

2. **스테이징 환경**
   - 테스트 서버
   - QA 테스트

3. **프로덕션 환경**
   - 클라우드 서비스 (AWS/GCP)
   - 모니터링 시스템
   - 로깅 시스템

## 유지보수
1. **문서화**
   - API 문서
   - 설정 가이드

2. **모니터링**
   - 성능 모니터링
   - 에러 추적
   - 사용자 행동 분석

3. **보안**
   - 정기적인 보안 업데이트
   - 취약점 스캔
   - 백업 시스템

## 실행 방법

1. 실행 스크립트 실행:
```bash
run.bat
```

2. 웹 브라우저에서 접속:
```
http://localhost:3000
``` 