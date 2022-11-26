from sqlalchemy import true
from website import create_app
if __name__ == "__name__":
    app= create_app()
    
    app.run(debug=True)