class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            refreshButton : document.querySelector('.refresh__button')
        }
        this.first=false;
        this.state = false;
        this.choice=0;
        this.messages = [];
    }
    
    
    display() {
        const {openButton, chatBox, sendButton,refreshButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        refreshButton.addEventListener('click', () => this.onRefreshButton(chatBox))
        
        //choiceButton.addEventListener('click', () => this.onChoiceButton(chatBox))  
        //[document.querySelector('.test__button1').querySelector('.test__button2')].forEach(item => {item.addEventListener('click', () => this.onChoiceButton(chatBox,this.id))})

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    //fonction d'affichage du chatbot
    toggleState(chatbox) {
        this.state = !this.state;
        if (this.first==false){
            this.first=true;

            let msg2 = { name: "Emi0",message: "Bonjour, sur quelles écoles souhaitez-vous vous renseigner ?" };//message: r.answer
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            const chatBox= document.querySelector('.chatbox__support');
            document.querySelector(".test__button1").addEventListener('click', () => this.onChoiceButton(chatBox,1)) 
            document.querySelector(".test__button2").addEventListener('click', () => this.onChoiceButton(chatBox,2)) 
            
        }
        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    //fonction pour envoyer un message
    onSendButton(chatbox) {
        
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }
        
        

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);
       
        //*********** */ test 
        // if(text1==="Salut" || text1==="Bonjour"){
        //     let msg2 = { name: "Emi", message: "Bonjour" };
        //     this.messages.push(msg2);
        // }
        // else{
        //     let msg2 = { name: "Emi", message: "Je m'appelle EMI, je suis là pour répondre à vos questions concernant l'ISEN." };
        //     this.messages.push(msg2);
        // }
        //********* */
        // this.updateChatText(chatbox);
        // textField.value = '';
        if(this.choice==1){ //si l'utilisateur a choisi l'isen
            fetch('http://127.0.0.1:5000/predictisen', {
                method: 'POST',
                body: JSON.stringify({ message: text1 }),
                mode: 'cors',
                headers: {
                'Content-Type': 'application/json'
                },
            })
            .then(r => r.json())
            .then(r => {
                let msg2 = { name: "Emi",message: r.answer };//message: r.answer
                this.messages.push(msg2);
                this.updateChatText(chatbox)
                textField.value = ''

            })
            .catch((error) => {
                console.error('Error:', error);
                this.updateChatText(chatbox)
                textField.value = ''
            });
        }
        else if(this.choice==2){ //si l'utilisateur a choisi l'IA Microsoft
            fetch('http://127.0.0.1:5000/predictiamic', {
                method: 'POST',
                body: JSON.stringify({ message: text1 }),
                mode: 'cors',
                headers: {
                'Content-Type': 'application/json'
                },
            })
            .then(r => r.json())
            .then(r => {
                let msg2 = { name: "Emi",message: r.answer };
                this.messages.push(msg2);
                this.updateChatText(chatbox)
                textField.value = ''

            })
            .catch((error) => {
                console.error('Error:', error);
                this.updateChatText(chatbox)
                textField.value = ''
            });
        }
        else{
            let msg2 = { name: "Emi0",message: "Veuillez d'abord sélectionner sur quelle école vous souhaitez-vous renseigner" };
            this.messages.push(msg2);
            this.updateChatText(chatbox) 
            const chatBox= document.querySelector('.chatbox__support');
            document.querySelector(".test__button1").addEventListener('click', () => this.onChoiceButton(chatBox,1)) ;
            document.querySelector(".test__button2").addEventListener('click', () => this.onChoiceButton(chatBox,2)) ;
        }
        document.querySelector('.chatbox__messages').scrollTop=0; // permet de revenir en bas de la conversation à chaque fois qu'un message est envoyé
        
    }
    //choix de l'école
    onChoiceButton(chatbox,id) {
        if(id==1){
            this.choice=1;
            let msg2 = { name: "Emi",message: "Comment puis-je vous renseigner sur l'ISEN?" };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
        }
        else{
            this.choice=2;
            let msg2 = { name: "Emi",message: "Comment puis-je vous renseigner sur l'école IA Microsoft?" };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
        }
        
    }
    //Rafraichir le chatbot
    onRefreshButton(chatbox,id) {
        var html = '<div></div>';
        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
        console.log(this.messages);
        //boucle permettant de supprimer l'historique
        var i;
        while ( (i = this.messages.shift()) !== undefined ) {
        }
        
        let msg2 = { name: "Emi0",message: "Bonjour, sur quelles écoles souhaitez-vous vous renseigner ?" };//message: r.answer
        this.messages.push(msg2);
        this.updateChatText(chatbox)
        const chatBox= document.querySelector('.chatbox__support'); 
        document.querySelector(".test__button1").addEventListener('click', () => this.onChoiceButton(chatBox,1));
        document.querySelector(".test__button2").addEventListener('click', () => this.onChoiceButton(chatBox,2));
        this.choice=0;
    }
    //permet l'affichage dans le chatbot
    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Emi")
            {
                
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
                
            }
            else if (item.name === "Emi0")
            {
                
                
                html += '<div class="test__button"><button id="test1" class="test__button1">ISEN</button><button id="test2" class="test__button2">IA Microsoft</button></div>'
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
                
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
                
            }
          });
        
        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}


const chatbox = new Chatbox();
chatbox.display();