from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

#Creates field that requires the dog's name and allows user to choose breed(s)
class DogBreedForm(FlaskForm):
    dogname = StringField("Dog name", validators = [DataRequired()])
    Affenpinschers =BooleanField(' Affenpinschers ')
    Afghan Hounds =BooleanField(' Afghan Hounds ')
    Airedale Terriers =BooleanField(' Airedale Terriers ')
    Akitas =BooleanField(' Akitas ')
    Alaskan Malamutes =BooleanField(' Alaskan Malamutes ')
    American English Coonhounds =BooleanField(' American English Coonhounds ')
    Toy American Eskimo Dog =BooleanField(' Toy American Eskimo Dog ')
    Miniature American Eskimo Dog =BooleanField(' Miniature American Eskimo Dog ')
    Standard American Eskimo Dog 25 =BooleanField(' Standard American Eskimo Dog 25 ')
    American Foxhounds =BooleanField(' American Foxhounds ')
    American Hairless Terriers =BooleanField(' American Hairless Terriers ')
    American Staffordshire Terriers =BooleanField(' American Staffordshire Terriers ')
    Anatolian Shepherd Dogs =BooleanField(' Anatolian Shepherd Dogs ')
    Australian Cattle Dogs =BooleanField(' Australian Cattle Dogs ')
    Australian Shepherds =BooleanField(' Australian Shepherds ')
    Australian Terriers =BooleanField(' Australian Terriers ')
    Basenjis =BooleanField(' Basenjis ')
    Basset Hounds =BooleanField(' Basset Hounds ')
    Beagles =BooleanField(' Beagles ')
    Bearded Collies =BooleanField(' Bearded Collies ')
    Beaucerons =BooleanField(' Beaucerons ')
    Bedlington Terriers =BooleanField(' Bedlington Terriers ')
    Belgian Malinois =BooleanField(' Belgian Malinois ')
    Belgian Sheepdogs =BooleanField(' Belgian Sheepdogs ')
    Belgian Tervuren =BooleanField(' Belgian Tervuren ')
    Bergamasco =BooleanField(' Bergamasco ')
    Berger Picards =BooleanField(' Berger Picards ')
    Bernese Mountain Dogs =BooleanField(' Bernese Mountain Dogs ')
    Bichons Frises =BooleanField(' Bichons Frises ')
    Black and Tan Coonhounds =BooleanField(' Black and Tan Coonhounds ')
    Black RussianTerriers =BooleanField(' Black RussianTerriers ')
    Bloodhounds =BooleanField(' Bloodhounds ')
    Bluetick Coonhounds =BooleanField(' Bluetick Coonhounds ')
    Boerboels =BooleanField(' Boerboels ')
    Border Collies =BooleanField(' Border Collies ')
    Border Terriers =BooleanField(' Border Terriers ')
    Borzois =BooleanField(' Borzois ')
    Boston Terriers =BooleanField(' Boston Terriers ')
    Bouviers des Flandres =BooleanField(' Bouviers des Flandres ')
    Boxers =BooleanField(' Boxers ')
    Briards =BooleanField(' Briards ')
    Brittanys =BooleanField(' Brittanys ')
    Brussels Griffons =BooleanField(' Brussels Griffons ')
    Bull Terriers =BooleanField(' Bull Terriers ')
    Bulldogs =BooleanField(' Bulldogs ')
    Bullmastiffs =BooleanField(' Bullmastiffs ')
    Cairn Terriers =BooleanField(' Cairn Terriers ')
    Canaan Dogs =BooleanField(' Canaan Dogs ')
    Cardigan Welsh Corgis =BooleanField(' Cardigan Welsh Corgis ')
    Cavalier King Charles Spaniels =BooleanField(' Cavalier King Charles Spaniels ')
    Cesky Terriers =BooleanField(' Cesky Terriers ')
    Chihuahuas =BooleanField(' Chihuahuas ')
    Chinese Crested =BooleanField(' Chinese Crested ')
    Chinese Shar Pei =BooleanField(' Chinese Shar Pei ')
    Chinooks =BooleanField(' Chinooks ')
    Chow Chows =BooleanField(' Chow Chows ')
    Cirnechi dell Etna =BooleanField(' Cirnechi dell Etna ')
    Collies =BooleanField(' Collies ')
    Coton de Tulear =BooleanField(' Coton de Tulear ')
    Standard Dachshunds =BooleanField(' Standard Dachshunds ')
    Miniature Dachunds =BooleanField(' Miniature Dachunds ')
    Dalmatians =BooleanField(' Dalmatians ')
    Dandie Dinmont Terriers =BooleanField(' Dandie Dinmont Terriers ')
    Doberman Pinschers =BooleanField(' Doberman Pinschers ')
    Dogues de Bordeaux =BooleanField(' Dogues de Bordeaux ')
    English Foxhounds =BooleanField(' English Foxhounds ')
    English Toy Spaniels =BooleanField(' English Toy Spaniels ')
    Entlebucher Mountain Dogs =BooleanField(' Entlebucher Mountain Dogs ')
    Finnish Lapphunds =BooleanField(' Finnish Lapphunds ')
    Finnish Spitz =BooleanField(' Finnish Spitz ')
    Fox Terriers =BooleanField(' Fox Terriers ')
    French Bulldogs =BooleanField(' French Bulldogs ')
    German Pinschers =BooleanField(' German Pinschers ')
    German Shepherd Dogs =BooleanField(' German Shepherd Dogs ')
    Giant Schnauzers =BooleanField(' Giant Schnauzers ')
    Glen of Imaal Terriers =BooleanField(' Glen of Imaal Terriers ')
    Great Danes =BooleanField(' Great Danes ')
    Great Pyrenees =BooleanField(' Great Pyrenees ')
    Greater Swiss Mountain Dogs =BooleanField(' Greater Swiss Mountain Dogs ')
    Greyhounds =BooleanField(' Greyhounds ')
    Harriers =BooleanField(' Harriers ')
    Havanese =BooleanField(' Havanese ')
    Ibizan Hounds =BooleanField(' Ibizan Hounds ')
    Icelandic Sheepdogs =BooleanField(' Icelandic Sheepdogs ')
    Irish Terriers =BooleanField(' Irish Terriers ')
    Irish Wolfhounds =BooleanField(' Irish Wolfhounds ')
    Italian Greyhounds =BooleanField(' Italian Greyhounds ')
    Japanese Chin =BooleanField(' Japanese Chin ')
    Keeshonden =BooleanField(' Keeshonden ')
    Kerry Blue Terriers =BooleanField(' Kerry Blue Terriers ')
    Komondor =BooleanField(' Komondor ')
    Kuvaszok =BooleanField(' Kuvaszok ')
    Lagotti Romagnoli =BooleanField(' Lagotti Romagnoli ')
    Lakeland Terriers =BooleanField(' Lakeland Terriers ')
    Leonbergers =BooleanField(' Leonbergers ')
    Lhasa Apsos =BooleanField(' Lhasa Apsos ')
    Lowchen =BooleanField(' Lowchen ')
    Maltese =BooleanField(' Maltese ')
    Toy Manchester Terriers =BooleanField(' Toy Manchester Terriers ')
    Standard Manchester Terriers =BooleanField(' Standard Manchester Terriers ')
    Mastiffs =BooleanField(' Mastiffs ')
    Miniature American Shepherds =BooleanField(' Miniature American Shepherds ')
    Miniature Bull Terriers =BooleanField(' Miniature Bull Terriers ')
    Miniature Pinschers =BooleanField(' Miniature Pinschers ')
    Miniature Schnauzers =BooleanField(' Miniature Schnauzers ')
    Neapolitan Mastiffs =BooleanField(' Neapolitan Mastiffs ')
    Newfoundlands =BooleanField(' Newfoundlands ')
    Norfolk Terriers =BooleanField(' Norfolk Terriers ')
    Norwegian Buhunds =BooleanField(' Norwegian Buhunds ')
    Norwegian Elkhounds =BooleanField(' Norwegian Elkhounds ')
    Norwegian Lundehunds =BooleanField(' Norwegian Lundehunds ')
    Norwich Terriers =BooleanField(' Norwich Terriers ')
    Old English Sheepdogs =BooleanField(' Old English Sheepdogs ')
    Otterhounds =BooleanField(' Otterhounds ')
    Papillons =BooleanField(' Papillons ')
    Parson Russell Terriers =BooleanField(' Parson Russell Terriers ')
    Pekingese =BooleanField(' Pekingese ')
    Pembroke Welsh Corgis =BooleanField(' Pembroke Welsh Corgis ')
    Petits Bassets Griffons Vendeens =BooleanField(' Petits Bassets Griffons Vendeens ')
    Pharaoh Hounds =BooleanField(' Pharaoh Hounds ')
    Plotts =BooleanField(' Plotts ')
    Pointers =BooleanField(' Pointers ')
    Pointers (German Shorthaired) =BooleanField(' Pointers (German Shorthaired) ')
    Pointers (German Wirehaired) =BooleanField(' Pointers (German Wirehaired) ')
    Polish Lowland Sheepdogs =BooleanField(' Polish Lowland Sheepdogs ')
    Pomeranians =BooleanField(' Pomeranians ')
    Toy Poodles =BooleanField(' Toy Poodles ')
    Miniature Poodles =BooleanField(' Miniature Poodles ')
    Standard Poodle =BooleanField(' Standard Poodle ')
    Portuguese Podengo Pequenos =BooleanField(' Portuguese Podengo Pequenos ')
    Portuguese Water Dogs =BooleanField(' Portuguese Water Dogs ')
    Pugs =BooleanField(' Pugs ')
    Pulik =BooleanField(' Pulik ')
    Pumik =BooleanField(' Pumik ')
    Pyrenean Shepherds =BooleanField(' Pyrenean Shepherds ')
    Rat Terriers =BooleanField(' Rat Terriers ')
    Redbone Coonhounds =BooleanField(' Redbone Coonhounds ')
    Retrievers (Chesapeake Bay) =BooleanField(' Retrievers (Chesapeake Bay) ')
    Retrievers (Curly Coated) =BooleanField(' Retrievers (Curly Coated) ')
    Retrievers (Flat Coated) =BooleanField(' Retrievers (Flat Coated) ')
    Retrievers (Golden) =BooleanField(' Retrievers (Golden) ')
    Retrievers (Labrador) =BooleanField(' Retrievers (Labrador) ')
    Retrievers (Nova Scotia Duck Tolling) =BooleanField(' Retrievers (Nova Scotia Duck Tolling) ')
    Rhodesian Ridgebacks =BooleanField(' Rhodesian Ridgebacks ')
    Rottweilers =BooleanField(' Rottweilers ')
    Russell Terriers =BooleanField(' Russell Terriers ')
    Salukis =BooleanField(' Salukis ')
    Samoyeds =BooleanField(' Samoyeds ')
    Schipperkes =BooleanField(' Schipperkes ')
    Scottish Deerhounds =BooleanField(' Scottish Deerhounds ')
    Scottish Terriers =BooleanField(' Scottish Terriers ')
    Sealyham Terriers =BooleanField(' Sealyham Terriers ')
    Setters (English) =BooleanField(' Setters (English) ')
    Setters (Gordon) =BooleanField(' Setters (Gordon) ')
    Setters (Irish Red and White) =BooleanField(' Setters (Irish Red and White) ')
    Setters (Irish) =BooleanField(' Setters (Irish) ')
    Shetland Sheepdogs =BooleanField(' Shetland Sheepdogs ')
    Shiba Inu =BooleanField(' Shiba Inu ')
    Shih Tzu =BooleanField(' Shih Tzu ')
    Siberian Huskies =BooleanField(' Siberian Huskies ')
    Silky Terriers =BooleanField(' Silky Terriers ')
    Skye Terriers =BooleanField(' Skye Terriers ')
    Sloughis =BooleanField(' Sloughis ')
    Soft Coated Wheaten Terriers =BooleanField(' Soft Coated Wheaten Terriers ')
    Spaniels (American Water) =BooleanField(' Spaniels (American Water) ')
    Spaniels (Boykin) =BooleanField(' Spaniels (Boykin) ')
    Spaniels (Clumber) =BooleanField(' Spaniels (Clumber) ')
    Spaniels (English Cocker) =BooleanField(' Spaniels (English Cocker) ')
    Spaniels (English Springer) =BooleanField(' Spaniels (English Springer) ')
    Spaniels (Field) =BooleanField(' Spaniels (Field) ')
    Spaniels (Irish Water) =BooleanField(' Spaniels (Irish Water) ')
    Spaniels (Sussex) =BooleanField(' Spaniels (Sussex) ')
    Spaniels (Welsh Springer) =BooleanField(' Spaniels (Welsh Springer) ')
    Spanish Water Dogs =BooleanField(' Spanish Water Dogs ')
    Spinoni Italiani =BooleanField(' Spinoni Italiani ')
    St. Bernards =BooleanField(' St. Bernards ')
    Staffordshire Bull Terriers =BooleanField(' Staffordshire Bull Terriers ')
    Standard Schnauzers =BooleanField(' Standard Schnauzers ')
    Swedish Vallhunds =BooleanField(' Swedish Vallhunds ')
    Tibetan Mastiffs =BooleanField(' Tibetan Mastiffs ')
    Tibetan Terriers =BooleanField(' Tibetan Terriers ')
    Tibetan Spaniel =BooleanField(' Tibetan Spaniel ')
    Toy Fox Terriers =BooleanField(' Toy Fox Terriers ')
    Treeing Walker Coonhounds =BooleanField(' Treeing Walker Coonhounds ')
    Vizslas =BooleanField(' Vizslas ')
    Weimaraners =BooleanField(' Weimaraners ')
    Welsh Terriers =BooleanField(' Welsh Terriers ')
    West Highland White Terriers =BooleanField(' West Highland White Terriers ')
    Whippets =BooleanField(' Whippets ')
    Wirehaired Pointing Griffons =BooleanField(' Wirehaired Pointing Griffons ')
    Wirehaired Vizslas =BooleanField(' Wirehaired Vizslas ')
    Toy Xoloitzcuintli =BooleanField(' Toy Xoloitzcuintli ')
    Miniature Xoloitzcuintli =BooleanField(' Miniature Xoloitzcuintli ')
    Standard Xoloitzcuintli =BooleanField(' Standard Xoloitzcuintli ')
    Yorkshire Terriers =BooleanField(' Yorkshire Terriers ')
    submit = SubmitField('Check weight')