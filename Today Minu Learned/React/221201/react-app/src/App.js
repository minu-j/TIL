import './App.css';
import {useState} from 'react'

function Header(props) {
  return (
    <header>
      <h1><a href="/" onClick={event => {
        event.preventDefault()
        props.onChangeMode()
      }}>{props.title}</a></h1>
    </header>
  )
}

function Nav(props) {
  const lis = []

  for (let i = 0; i < props.topics.length; i++) {
    const topic = props.topics[i]
    lis.push(
      <li key={'topic' + topic.id}>
        <a id={topic.id} href={'/read/' + topic.id} onClick={ event => {
          event.preventDefault()
          props.onChangeMode(event.target.id)
        }}>
          {topic.title}
        </a>
      </li>)
  }

  return (
    <nav>
        <ol>
          {lis}
        </ol>
      </nav>
  )
}

function Article(props) {
  return (
    <article>
        <h2>{props.title}</h2>
        {props.content}
      </article>
  )
}

function App() {
  // state
  let [ mode, setMode ] = useState('WELCOME')
  let [ id, setId ] = useState(null)
  let [ topics, setTopics ] = useState([
    { id: 1, title: 'html', body: 'html is ...' },
    { id: 2, title: 'css', body: 'css is ...' },
    { id: 3, title: 'js', body: 'js is ...' }
  ])

  let content = null
  let contextControl = null
  
  function Create(props) {
    return (
      <article>
        <h2>Create</h2>
        <form onSubmit={ event => {
          event.preventDefault()
          const title = event.target.title.value
          const body = event.target.body.value
          props.onCreate(title, body)
        }}>
          <div>
            <input type="text" name='title' placeholder='title'/>
          </div>
          <div>
            <textarea name="body" placeholder='body'></textarea>
          </div>
          <input type="submit" value="작성" />
          
        </form>
      </article>
    )
  }

  function Update(props) {
    const [ title, setTitle ] = useState(props.title)
    const [ body, setBody ] = useState(props.body)
    return (
      <article>
        <h2>Update</h2>
        <form onSubmit={ event => {
          event.preventDefault()
          const title = event.target.title.value
          const body = event.target.body.value
          props.onUpdate(title, body)
        }}>
          <div>
            <input type="text" name='title' value={title} onChange={ event => {
              setTitle(event.target.value)
            }}/>
          </div>
          <div>
            <textarea name="body" value={body} onChange={ event => {
              setBody(event.target.value)
            }}></textarea>
          </div>
          <input type="submit" value="수정"/>
        </form>
      </article>
    )
  }

  if (mode === 'WELCOME') {
    content = <Article title="Welcme" content="Hello, WEB"></Article>

  } else if (mode === 'READ') {
    for (let i = 0; i < topics.length; i++) {
      if (parseInt(id) === topics[i].id) {
        content = <Article title={topics[i].title} content={topics[i].body}></Article>
        break
      }      
    }
    contextControl = <div>
      <li><a href={'/update/' + id} onClick={ event => {
        event.preventDefault()
        setMode('UPDATE')
      }}>Update</a></li>
      <button onClick={() => {
        const newTopics = []
        for (let i = 0; i < topics.length; i++) {
          if (parseInt(id) !== topics[i].id) {
            newTopics.push(topics[i])
          }
        }
        setTopics(newTopics)
        setMode('WELCOME')
      }}>Delete</button>
    </div>

  } else if (mode === 'CREATE') {
    content = <Create onCreate={(title, body) => {
      const nextId = topics.length + 1
      const newTopic = {
        id: nextId,
        title: title,
        body: body
      }
      const newTopics = [...topics]
      newTopics.push(newTopic)
      setTopics(newTopics)
      setMode('READ')
      setId(nextId)
    }}></Create>

  } else if (mode === 'UPDATE') {
    let title, body = null
    for (let i = 0; i < topics.length; i++) {
      if (parseInt(id) === topics[i].id) {
        title = topics[i].title
        body = topics[i].body
        break
      }      
    }
    content = <Update title={title} body={body} onUpdate={(title, body) => {
      const updatedTopic = {
        id: parseInt(id),
        title: title,
        body: body
      }
      const newTopics = [...topics]
      for (let i = 0; i < newTopics.length; i++) {
        if (parseInt(id) === newTopics[i].id) {
          newTopics[i] = updatedTopic
          break
        }
      }
      setTopics(newTopics)
      setMode('READ')
    }}></Update>
  }


  return (
    <div>
      <Header title="WEB" onChangeMode={() => {
        setMode('WELCOME')
      }}></Header>
      <Nav topics={topics} onChangeMode={(id) => {
        setMode('READ')
        setId(id)
      }}></Nav>
      {content}
      <ul>
        <li><a href="/create" onClick={event => {
        event.preventDefault()
        setMode('CREATE')
      }}>Create</a></li>
        {contextControl}
      </ul>
    </div>
  );
}

export default App;
