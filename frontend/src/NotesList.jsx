function NotesList({ notes }){
    return (
        <ul>
            {notes.map((note) => (
            <li key={note.id}>{note.title}</li>
            ))}
        </ul>
    );

}

export default NotesList;