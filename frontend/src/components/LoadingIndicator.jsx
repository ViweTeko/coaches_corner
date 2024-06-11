/* This script shows a loading indicator when user presses
  register and login buttons */
import "../styles/LoadingIndicator.css";

const LoadingIndicator = () => {
  return (
    <div className="loading-container">
      <div className="loader"></div>
    </div>
  );
};

export default LoadingIndicator;
