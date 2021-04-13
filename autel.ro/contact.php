
<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="utf-8" />
        <title>Autel Online - Contact</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Doriți să realizați o diagnoză completă a automobilului? Cu ajutorul nostru puteți avea acces la cele mai bune uneltele de diagnoză Autel. 
        Efectuați o diagnoză inteligentă și completă  a automobilului personal și nu numai." />
        <meta name="keywords" content="Autel, diagnoză, programare chei, tmps, unelte, diagnoză, autelonline" />

        <?php include 'php/head.php' ?>
   
    </head>

    <body>

        <?php include 'php/header.php'?>
        
        <section class="bg-half bg-light d-table w-100" style="background: url('img/c002.jpg') center center;">
            <div class="bg-overlay"></div>
            <div class="bg-overlay"></div>
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-12 text-center">
                        <div class="page-next-level">
                            <h4 class="title text-white">Contactează-ne</h4>
                            <div class="page-next">
                                <nav aria-label="breadcrumb" class="d-inline-block">
                                    <ul class="breadcrumb bg-white rounded shadow mb-0">
                                        <li class="breadcrumb-item"><a href="index.php">AutelOnline.ro</a></li>
                                        <li class="breadcrumb-item"><a href="contact.php">Contact</a></li>
                                    </ul>
                                </nav>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <div class="position-relative">
            <div class="shape overflow-hidden text-white">
                <svg viewBox="0 0 2880 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M0 48H1437.5H2880V0H2160C1442.5 52 720 0 720 0H0V48Z" fill="currentColor"></path>
                </svg>
            </div>
        </div>

        <section class="section pb-0">
            <div class="container">
                <div class="row">
                    <div class="col-md-4">
                        <div class="card contact-detail text-center border-0">
                            <div class="card-body p-0">
                                <div class="icon">
                                    <img src="img/icon/bitcoin.svg" class="avatar avatar-small" alt="">
                                </div>
                                <div class="content mt-3">
                                    <h4 class="title font-weight-bold">Telefon</h4>
                                    <p class="text-muted">Pentru mai multe detalii ne găsiți la acest număr de telefon</p>
                                    <a href="tel:+40731-649-617" class="text-primary">+40 731 649 617</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="col-md-4 mt-4 mt-sm-0 pt-2 pt-sm-0">
                        <div class="card contact-detail text-center border-0">
                            <div class="card-body p-0">
                                <div class="icon">
                                    <img src="img/icon/Email.svg" class="avatar avatar-small" alt="">
                                </div>
                                <div class="content mt-3">
                                    <h4 class="title font-weight-bold">Email</h4>
                                    <p class="text-muted">Pentru posibile comenzi sau mai multe informații</p>
                                    <a href="mailto:contact@autelonline.ro" class="text-primary">contact@autelonline.ro</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="col-md-4 mt-4 mt-sm-0 pt-2 pt-sm-0">
                        <div class="card contact-detail text-center border-0">
                            <div class="card-body p-0">
                                <div class="icon">
                                    <img src="img/icon/location.svg" class="avatar avatar-small" alt="">
                                </div>
                                <div class="content mt-3">
                                    <h4 class="title font-weight-bold">Adresă</h4>
                                    <p class="text-muted">Bd. Iuliu Maniu <br>București, Romania</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- TODO make form work -->
            <div class="container mt-100 mt-60">
                <div class="row align-items-center">
                    <div class="col-lg-7 col-md-6 pt-2 pt-sm-0 order-2 order-md-1">
                        <div class="card shadow rounded border-0">
                            <div class="card-body py-5">
                                <h4 class="card-title">Scrie-ne !</h4>
                                <div class="custom-form mt-4">
                                    <div id="message"></div>
                                    <form method="post" action="php/contact.php" name="contact-form" id="contact-form">
                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group position-relative">
                                                    <label>Nume <span class="text-danger">*</span></label>
                                                    <i data-feather="user" class="fea icon-sm icons"></i>
                                                    <input name="name" id="name" type="text" class="form-control pl-5" placeholder="Numele tau :">
                                                </div>
                                            </div><!--end col-->
                                            <div class="col-md-6">
                                                <div class="form-group position-relative">
                                                    <label>Email <span class="text-danger">*</span></label>
                                                    <i data-feather="mail" class="fea icon-sm icons"></i>
                                                    <input name="email" id="email" type="email" class="form-control pl-5" placeholder="Emailul tau :">
                                                </div> 
                                            </div><!--end col-->
                                            <div class="col-md-12">
                                                <div class="form-group position-relative">
                                                    <label>Subiect</label>
                                                    <i data-feather="book" class="fea icon-sm icons"></i>
                                                    <input name="subject" id="subject" type="text" class="form-control pl-5" placeholder="Subiect">
                                                </div>                                                                               
                                            </div><!--end col-->
                                            <div class="col-md-12">
                                                <div class="form-group position-relative">
                                                    <label>Mesaj</label>
                                                    <i data-feather="message-circle" class="fea icon-sm icons"></i>
                                                    <textarea name="comments" id="comments" rows="4" class="form-control pl-5" placeholder="Mesajul tau :"></textarea>
                                                </div>
                                            </div>
                                        </div><!--end row-->
                                        <div class="row">
                                            <div class="col-sm-12 text-center">
                                                <input type="submit" id="submit" name="send" class="submitBnt btn btn-primary btn-block" value="Send Message">
                                                <div id="simple-msg"></div>
                                            </div><!--end col-->
                                        </div><!--end row-->
                                    </form><!--end form--> 
                                </div><!--end custom-form-->
                            </div>
                        </div>
                    </div><!--end col-->

                    <div class="col-lg-5 col-md-6 order-1 order-md-2">
                        <div class="card border-0">
                            <div class="card-body p-0">
                                <img src="img/certificates/cert_1.jpg" class="img-fluid" alt="" width="400" height="700">
                            </div>
                        </div>
                    </div><!--end col-->
                </div><!--end row-->
            </div><!--end container-->            

            <div class="container-fluid mt-100 mt-60"></div>
        </section>

        <?php include 'php/footer.php'?>

    </body>
</html>