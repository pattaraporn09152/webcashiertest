function HelloMessage({ name }) {
  return <div>สวัสดี {name}</div>;
}

ReactDOM.render(
  <HelloMessage name="วิทยา คอม" />,
  document.getElementById('container')
);
