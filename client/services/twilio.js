// const Chat = require('twilio-chat');

// const token = ""
//
// Chat.Client.create(token).then(client => {
//     // Use client
// });
//

const TwilioClient = () => {
    return {
        createChat() {
            return fetch("/api/twilio/chat", {
                method: "POST"
            })
        }
    }
}


export default TwilioClient
