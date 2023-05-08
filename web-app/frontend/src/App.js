import React, {useState, useEffect} from 'react'

function App() {
  const [memberData, setmemberData] = useState([])

  useEffect (() => {
    fetch('http://localhost:5001/members', {
      'methods' : 'GET',
      headers: {
        'Content-Type': 'applications/json',
        'Authorization': `Bearer`,
      }
    })
    .then(res => res.json())
    .then(memberData => {
      setmemberData(memberData)
      console.log(memberData)
      }
    )
  },[])

  return (
  <div>
    {(typeof memberData.members === 'undefined') ? (
      <p>loading...</p>
      ) : (
        memberData.members.map((member, i) => (
        <p key={i}>{member}</p>
        ))
      )}
  </div>
  )
}
export default App