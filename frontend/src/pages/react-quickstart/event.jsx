function Event(){
    function handleclick(){
        alert("you clicked me")
    }

    return (
        <button onClick={handleclick}>click me</button>
    )
}
export default Event