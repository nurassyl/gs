import React from 'react';
import ReactDOM from 'react-dom';

import 'jquery';
import 'bootstrap';
import 'bootstrap/js/dist/util';
import 'bootstrap/js/dist/dropdown';

import './styles.sass';

class App extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			converterSelection: 'cyrillic-latin',
			input: 'Қазақ тілі',
			output: ''
		}
		this.translateHandle = this.translateHandle.bind(this);
		this.inputChangeHandle = this.inputChangeHandle.bind(this);
		this.converterSelectionChangeHandle = this.converterSelectionChangeHandle.bind(this);
	}
	translateHandle(e) {
		this.setState({
			output: this.state.input
		});
	}
	inputChangeHandle(e) {
		this.setState({
			input: e.target.value
		})
	}
	converterSelectionChangeHandle(e) {
		this.setState({
			converterSelection: e.target.value
		})
	}
	render() {
		return (
			<div>
				<div className="options">
					<div className="container">
						<div className="form-inline">
							<div className="form-group convertor-selection">
								<select className="form-control select-converter" defaultValue={this.state.converterSelection} onChange={this.converterSelectionChangeHandle}>
									<option value="cyrillic-latin">кириллица > латын</option>
									<option value="cyrillic-tote">кириллица > төте</option>
									<option value="latin-cyrillic">латын > кириллица</option>
									<option value="latin-tote">латын > төте</option>
									<option value="tote-latin">төте > латын</option>
									<option value="tote-cyrillic">төте > кириллица</option>
								</select>
							</div>
							<div className="form-group">
								<button type="button" className="btn btn-primary" onClick={this.translateHandle}>Аудару</button>
							</div>
						</div>
					</div>
				</div>
				<div  className="container content">
					<hr/>
					<div className="row">
						<div className="col-lg-6 input">
							<textarea className="form-control" placeholder="Мәтінді жазыңыз.." max-length="7000" defaultValue={this.state.input} onChange={this.inputChangeHandle}></textarea>
						</div>
						<div className="col-lg-6 output">
							<div>{this.state.output}</div>
						</div>
					</div>
				</div>
				<footer className="text-center text-muted">
					<hr/>
					<a>Nurasyl Aldan</a>
				</footer>
			</div>
		);
	}
}

ReactDOM.render(
	<App />,
	document.getElementById("app")
);
