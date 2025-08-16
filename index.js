const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const MemoryStore = require('memorystore')(session); // 세션 저장소

const app = express();
const port = 3000;

// 임시 유저 저장소
const users = [];

// 세션 저장소 설정 (MemoryStore 사용)
const sessionStore = new MemoryStore({
  checkPeriod: 1000 * 60 * 60 // 1시간마다 만료된 세션 정리
});

app.use(bodyParser.json());

app.use(session({
  secret: 'my-secret-key',
  resave: false,
  saveUninitialized: false,
  store: sessionStore,
  cookie: {
    httpOnly: true,
    secure: false,
    maxAge: 1000 * 60 * 30 // 30분
  }
}));

// ✅ 회원가입
app.post('/register', (req, res) => {
  const { username, password } = req.body;
  const existingUser = users.find(user => user.username === username);

  if (existingUser) {
    return res.status(400).json({ message: 'User already exists.' });
  }

  users.push({ username, password });
  return res.status(201).json({ message: 'Registration successful.' });
});

// ✅ 로그인 (세션 ID 수동 전달)
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username && u.password === password);

  if (!user) {
    return res.status(401).json({ message: 'Login failed' });
  }

  // 수동으로 세션 생성
  req.session.regenerate(err => {
    if (err) return res.status(500).json({ message: 'Session error' });

    req.session.user = { username };

    // 클라이언트에게 세션 ID를 명시적으로 전달 (Set-Cookie 대신)
    return res.json({
      message: 'Login successful',
      sessionId: req.sessionID // 클라이언트가 이 값을 저장해야 함
    });
  });
});

// ✅ 마이페이지 (세션 ID를 수동으로 헤더로 전달)
app.get('/mypage', (req, res) => {
  const sessionId = req.headers['x-session-id']; // 세션 ID를 헤더로 받음

  if (!sessionId) {
    return res.status(401).json({ message: 'Session ID is required' });
  }

  // 세션 저장소에서 세션 직접 조회
  sessionStore.get(sessionId, (err, sessionData) => {
    if (err || !sessionData || !sessionData.user) {
      return res.status(401).json({ message: 'Invalid or expired session' });
    }

    return res.json({
      message: 'Mypage access granted',
      user: sessionData.user
    });
  });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
