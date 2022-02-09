import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import TodoForm from './components/TodoForm.js'
import TodoList from './components/Todo.js'
import LoginForm from './components/Auth.js'
import AppMenu from './components/Menu.js'
import AppFooter from './components/Footer.js'
import axios from 'axios'
import {HashRouter, BrowserRouter, Route, Routes, Link, Switch, Redirect} from 'react-router-dom'
import Cookies from 'universal-cookie';


const NotFound404 = ({ location }) => {
  return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'todo': [],
           'projects' : [],
           'token': ''
       }
   }



  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token': token}, ()=>this.load_data())
  }

  is_authenticated() {
    return this.state.token != ''
  }

  logout() {
    this.set_token('')
  }

  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token': token}, ()=>this.load_data())
  }

  get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
    .then(response => {
        this.set_token(response.data['token'])
    }).catch(error => alert('Неверный логин или пароль'))
  }

  get_headers() {
    let headers = {
      'Content-Type': 'application/json'
    }
  if (this.is_authenticated())
    {
        headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
  }

  deleteProject(id) {
    const headers = this.get_headers()
    axios.delete(`http://127.0.0.1:8000/api/projects/${id}`, {headers})
        .then(response => {
          this.setState({projects: this.state.projects.filter((project)=>project.id !== id)})
        }).catch(error => console.log(error))
  }

  deleteTodo(id) {
    const headers = this.get_headers()
    axios.delete(`http://127.0.0.1:8000/api/doto/${id}`, {headers})
        .then(response => {
          this.setState({todo: this.state.todo.filter((todo)=>todo.id !== id)})
        }).catch(error => console.log(error))
  }

  createTodo(text, create_date, update_date, is_active, project, user) {
    console.log(text)
    const headers = this.get_headers()
    const data = {text: text, create_date: create_date, update_date: update_date, is_active:is_active, project:project}
    axios.post('http://127.0.0.1:8000/api/doto/', data, {headers, headers})
        .then(response => {
          let new_todo = response.data
          const project = this.state.projects.filter((project) => project.id === new_todo.project)[0]
          new_todo.project = project
          this.setState({projects: [...this.state.projects, new_todo]})
          const user = this.state.users.filter((user) => user.uuid === new_todo.user)[0]
          new_todo.user = user
          this.setState({users: [...this.state.users, new_todo]})
        }).catch(error => console.log(error))


  }


  load_data() {

    const headers = this.get_headers()


    axios.get('http://127.0.0.1:8000/api/users/', {headers})
        .then(response => {
            this.setState({users: response.data})
        }).catch(error => {
          console.log(error)
          this.setState({users: []})
        })

    axios.get('http://127.0.0.1:8000/api/projects/', {headers})
        .then(response => {
            this.setState({projects: response.data})
        }).catch(error => {
          console.log(error)
          this.setState({projects: []})
        })

    axios.get('http://127.0.0.1:8000/api/doto/', {headers})
        .then(response => {
            this.setState({todo: response.data})
        }).catch(error => {
          console.log(error)
          this.setState({todo: []})
        })
  }


  componentDidMount() {
    this.get_token_from_storage()
  }


   render () {
       return (
       <div className="App">
           <BrowserRouter>
           <nav>
              <ul>
                <li>
                  <Link to='/users'>Users</Link>
                </li>
                <li>
                  <Link to='/projects'>Projects</Link>
                </li>
                <li>
                  <Link to='/todo'>ToDo</Link>
                </li>
                <li>
                    {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                </li>
              </ul>
            </nav>
               <Routes>
               <Route exact path='/users' element={<UserList users={this.state.users} />}  />
               <Route exact path='/projects' element={<ProjectList projects={this.state.projects} deleteProject={(id)=>this.deleteProject(id)} />}  />
               <Route exact path='/todo/create' element={<TodoForm projects={this.state.projects} users={this.state.users} createTodo={(text, create_date, update_date, is_active, project, user) => this.createTodo(text, create_date, update_date, is_active, project, user)}/>}  />
               <Route exact path='/todo' element={<TodoList todo={this.state.todo} deleteTodo={(id)=>this.deleteTodo(id)} />} />
               <Route exact path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
               <Route component={NotFound404} />

               </Routes>

           </BrowserRouter>
       </div>
       )
   }


}


export default App;