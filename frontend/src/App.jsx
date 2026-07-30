import { useState, useEffect } from 'react'
import LoginForm from './LoginForm';
import NotesList from './NotesList';

function App() {
  const [token, setToken] = useState(null);

  return (
    <div>
      {token ? <NotesList token={token} /> : <LoginForm onLogin={setToken} />} 
      
    </div>
  )
}

export default App;
