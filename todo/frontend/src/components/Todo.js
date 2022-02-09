import React from 'react'
import {HashRouter, BrowserRouter, Route, Routes, Link, Switch, Redirect} from 'react-router-dom'

const TodoItem = ({todo, deleteTodo}) => {
   return (
       <tr>
           <td>
               {todo.text}
           </td>
           <td>
               {todo.create_date}
           </td>
           <td>
               {todo.update_date}
           </td>
           <td>
               {todo.is_active}
           </td>
           <td>
               {todo.user}
           </td>
           <td><button onClick={()=>deleteTodo(todo.id)} type='button'>Delete</button></td>
       </tr>
   )
}


const TodoList = ({todo, deleteTodo}) => {
   return (
   <div>
       <table>
           <th>
               ToDo text
           </th>
           <th>
               Create date
           </th>
           <th>
               Update date
           </th>
           <th>
               Is active
           </th>
           <th>
               User
           </th>
           {todo.map((todo) => <TodoItem todo={todo} deleteTodo={deleteTodo} />)}
       </table>
       <Link to='/todo/create'>Create</Link>
   </div>
   )
}


export default TodoList