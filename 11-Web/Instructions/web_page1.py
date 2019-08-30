<DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Bootstrap Components</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
​
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
​
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                  <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Data Link</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                     Comparison
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                      <a class="dropdown-item" href="#">Latitude Vs Humidity</a>
                      <a class="dropdown-item" href="#">Latitude Vs Max Temperature</a>
                      <div class="dropdown-divider"></div>
                      <a class="dropdown-item" href="#">Latitude Vs Cloudiness</a>
                    </div>
                  </li>
                  <li class="nav-item">
                        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true"></a>
                      </li>
                    </ul>
                    <form class="form-inline my-2 my-lg-0">
                      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                    </form>
                  </div>
                </nav>
                <div class="container">
                        <div class="jumbotron">
                          <h1 class="display-4">Latitude</h1>
                          <p class="lead">Summary of DataWork</p>
                          <hr class="my-4">
                          <p>Climate Data Online (CDO) provides free access to NCDC's archive of global historical weather and climate data in addition to station history information. These data include quality controlled daily, monthly, seasonal, and yearly measurements of temperature, precipitation, wind, and degree days as well as radar data and 30-year Climate Normals. 
                                Climate Data Online (CDO) provides free access to NCDC's archive of global historical weather and climate data in addition to station history information. These data include quality controlled daily, monthly, seasonal, and yearly measurements of temperature, precipitation, wind, and degree days as well as radar data and 30-year Climate Normals. 
                                Climate Data Online (CDO) provides free access to NCDC's archive of global historical weather and climate data in addition to station history information. These data include quality controlled daily, monthly, seasonal, and yearly measurements of temperature, precipitation, wind, and degree days as well as radar data and 30-year Climate Normals. 
​
                          </p>
                          <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
                        </div>
                      </div>        
                      <div class="container">
                            <h3 class="text-center">Summary Data Pictures</h3>
                              <div class="row">
                                  <div class="col-md-4">
                                    <div class="thumbnail">
                                      <img src="https://i.ytimg.com/vi/tntOCGkgt98/maxresdefault.jpg" alt="..." class="img-thumbnail">
                                    </div>
                                    <div class="caption">
                                        <h3>Cloudiness</h3>
                                        
                                        <p><a href="#" class="btn btn-primary" role="button">Button</a> 
                                      </div>
                                  </div>
                                  <div class="col-md-4">
                                      <div class="thumbnail">
                                        <img src="https://i.ytimg.com/vi/tntOCGkgt98/maxresdefault.jpg" alt="..." class="img-thumbnail">
                                      </div>
                                    <div class="caption">
                                        <h3>Humidity</h3>
                    
                                        <p><a href="#" class="btn btn-primary" role="button">Button</a> 
                                    </div>
                                  </div>
                                  <div class="col-md-4">
                                      <div class="thumbnail">
                                        <img src="https://i.ytimg.com/vi/tntOCGkgt98/maxresdefault.jpg" alt="..." class="img-thumbnail">
                                      </div>
                                      <div class="caption">
                                          <h3>Max Temperature</h3>
                                          
                                          <p><a href="#" class="btn btn-primary" role="button">Button</a> 
                                    </div>
                                  </div>
                              </div>
        
</body>
</html>