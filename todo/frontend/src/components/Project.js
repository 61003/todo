import React from 'react'

const ProjectItem = ({project}) => {
   return (
       <tr>
           <td>
               {project.name}
           </td>
           <td>
               {project.repo_url}
           </td>
       </tr>
   )
}

const ProjectList = ({projects}) => {
   return (
       <table>
           <th>
               Name
           </th>
           <th>
               Url
           </th>
           {projects.map((project) => <ProjectItem project={project} />)}
       </table>
   )
}


export default ProjectList