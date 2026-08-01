import { useState, useEffect } from 'react'
import LoginForm from './LoginForm';
import NotesList from './NotesList';
import AddNoteForm from './AddNoteForm'

function App() {
  const [token, setToken] = useState(null);
  const [notes, setNotes] = useState([]);

    useEffect(()=>{
        if(!token) return;
    
        async function fetchNotes(){
          const response = await fetch('http://localhost:5001/api/notes', {
            headers: {"Authorization": `Bearer ${token}`}
          });
          const data = await response.json();
          setNotes(data);
    
        }
        fetchNotes();
    }, [token])

  return (
    <div>
      {token ? (
      <div>
        <AddNoteForm token={token} setNotes={setNotes}/>
        <NotesList notes={notes} />
      </div>
      ) : (
        <LoginForm onLogin={setToken} />
      )} 
      
    </div>
  )
}

export default App;
