import { useState, useEffect } from 'react'

function NotesList({token}){
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
        <ul>
            {notes.map((note) => (
            <li key={note.id}>{note.title}</li>
            ))}
        </ul>
    );

}

export default NotesList;