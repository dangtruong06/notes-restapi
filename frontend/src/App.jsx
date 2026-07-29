import { useState } from 'react'

function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState(null);

  async function handleLogin(e){
    e.preventDefault();

    const response = await fetch('http://localhost:5001/api/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email, password})
    });

    const data = await response.json();
    setToken(data.access_token);
  }

  return (
    <form onSubmit={handleLogin}>
      <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="email"/>
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="password"/>
      <button type="submit">Login</button>
      <p>{token}</p>
    </form>
  )
}

export default App;
