import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import TodoList from './components/Todo.js'
import AppMenu from './components/Menu.js'
import AppFooter from './components/Footer.js'
import axios from 'axios'
import {HashRouter, BrowserRouter, Route, Routes, Link, Switch, Redirect} from 'react-router-dom'


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'project': [],
           'todo': []
       }
   }

   componentDidMount() {
   axios.get('http://127.0.0.1:8000/api/users')
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users
               }
           )
       }).catch(error => console.log(error))

   axios.get('http://127.0.0.1:8000/api/projects')
       .then(response => {
           const project = response.data
               this.setState(
               {
                   'project': project
               }
           )
       }).catch(error => console.log(error))

   axios.get('http://127.0.0.1:8000/api/doto')
       .then(response => {
           const todo = response.data
               this.setState(
               {
                   'todo': todo
               }
           )
       }).catch(error => console.log(error))

   }


   render () {
       return (
       <div className="App">
           <BrowserRouter>
               <Routes>
               <Route exact path='/users' element={<UserList users={this.state.users} />}  />
               <Route exact path='/projects' element={<ProjectList project={this.state.project} />}  />
               <Route exact path='/todo' element={<TodoList todo={this.state.todo} />} />
               </Routes>
           </BrowserRouter>
       </div>
       )
   }


}


export default App;