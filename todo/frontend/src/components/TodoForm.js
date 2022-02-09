import React from 'react'


class TodoForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {text: '', create_date: '', update_date: '', is_active: '', project: props.projects[0]?.id, user: props.users[0]?.uuid}

    }

    handleChange(event)
    {

        this.setState(
                {
                    [event.target.name]: event.target.value
                }
            );
    }

    handleSubmit(event) {
      this.props.createTodo(this.state.text, this.state.create_date, this.update_date.user, this.is_active, this.project, this.user)
      event.preventDefault()
    }

    render() {
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>

            <div className="form-group">
            <label htmlFor="text">text</label>
                <input type="text" className="form-control" name="text" value={this.state.text} onChange={(event)=>this.handleChange(event)} />
            </div>

            <div className="form-group">
            <label htmlFor="create_date">create_date</label>
                <input type="text" className="form-control" name="create_date" value={this.state.create_date} onChange={(event)=>this.handleChange(event)} />
            </div>

            <div className="form-group">
            <label htmlFor="update_date">update_date</label>
                <input type="text" className="form-control" name="update_date" value={this.state.update_date} onChange={(event)=>this.handleChange(event)} />
            </div>

            <div className="form-group">
            <label htmlFor="is_active">is_active</label>
                <input type="text" className="form-control" name="is_active" value={this.state.is_active} onChange={(event)=>this.handleChange(event)} />
            </div>

            <div className="form-group">
            <label htmlFor="project">project</label>
            <select name="project" className='form-control' onChange={(event)=>this.handleChange(event)}>
                {this.props.projects.map((project)=><option value={project.id}>{project.name}</option>)}
            </select>

            </div>

            <div className="form-group">
            <label htmlFor="user">user</label>
            <select name="user" className='form-control' onChange={(event)=>this.handleChange(event)}>
                {this.props.users.map((user)=><option value={user.uuid}>{user.username}</option>)}
            </select>

            </div>


          <input type="submit" className="btn btn-primary" value="Save" />

        </form>
      );
    }
  }

  export default TodoForm