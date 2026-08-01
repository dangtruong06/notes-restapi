import { useState } from 'react'

function AddNoteForm({token, setNotes}){
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    async function addNote(e){
        e.preventDefault();

        const response = await fetch('http://localhost:5001/api/notes', {
            method: 'POST',
            headers: {'Authorization': `Bearer ${token}`,
                      'Content-Type': 'application/json'},
            body: JSON.stringify({title, content}),

        });
        const data = await response.json()
        setNotes(previousNotes => [...previousNotes, data]);

    }

    return(
        <form onSubmit={ addNote }>
            <input value={title} onChange={(e) => setTitle(e.target.value)}/>
            <input value={content} onChange={(e) => setContent(e.target.value)}/>
            <input type='Submit'/>submit
        </form>
    )
}

export default AddNoteForm;