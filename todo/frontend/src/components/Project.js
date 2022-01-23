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


const ProjectList = ({project}) => {
   return (
       <table>
           <th>
               Project name
           </th>
           <th>
               Repo url
           </th>
           {project.map((project) => <ProjectItem project={project} />)}
       </table>
   )
}


export default ProjectList