import React, { Component } from 'react';
import styles from './chat.scss'

import TwilioClient from 'services/twilio'


function ChatContainer() {
    TwilioClient().getToken()

    return (
        <div className={styles.chatContainer}>
            <div className={styles.messages}>
            </div>
            <div className={styles.messageWindow}>
            </div>
        </div>
    );
}


export default ChatContainer
