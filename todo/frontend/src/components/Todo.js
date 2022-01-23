import React from 'react'


const TodoItem = ({todo}) => {
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
       </tr>
   )
}


const TodoList = ({todo}) => {
   return (
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
           {todo.map((todo) => <TodoItem todo={todo} />)}
       </table>
   )
}


export default TodoList