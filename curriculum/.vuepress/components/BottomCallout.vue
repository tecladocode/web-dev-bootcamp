<script>
export default {
  props: ['title', 'subtitle']
}
</script>

<template>
    <div class="bottom-callout">
        <div class="bottom-callout__content">
        <h3 class="bottom-callout__title">
            <span v-if="title">{{ title }}</span>
            <span v-else-if="!title">Enjoyed this article?<br/>You'll love the complete video course!</span>
        </h3>
        <p v-if="subtitle" class="bottom-callout__text">
            {{ subtitle }}
        </p>
        <ul class="bottom-callout__features">
            <li class="bottom-callout__feature">
                <svg class="bottom-callout__feature-icon hover-green" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  
<g transform="matrix(1,0,0,1,0,0)"><g>
    <rect x="0.73" y="2.5" width="22.54" height="15.5" rx="2" style="fill: none;stroke: #ffffff;stroke-linecap: round;stroke-linejoin: round;stroke-width: 1.5px"></rect>
    <path d="M10.22,7.15a.5.5,0,0,0-.74.44v5.32a.5.5,0,0,0,.74.44l4.94-2.66a.49.49,0,0,0,0-.88Z" style="stroke: #ffffff;stroke-linecap: round;stroke-linejoin: round;stroke-width: 1.5px"></path>
    <line x1="19.48" y1="21.5" x2="4.48" y2="21.5" style="fill: none;stroke: #ffffff;stroke-linecap: round;stroke-linejoin: round;stroke-width: 1.5px"></line>
  </g></g></svg>
                <span class="bottom-callout__feature-text">
                    Complete video lessons for each topic
                </span>
            </li>
            <li class="bottom-callout__feature">
                <svg class="bottom-callout__feature-icon hover-gold" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <g transform="matrix(1,0,0,1,0,0)">
                    <path d="M12 23.242L18 17.242 18 6.742 12 0.742 6 6.742 6 17.242 12 23.242z" fill="none" stroke="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                    <path d="M12 0.742L12 23.242" fill="none" stroke="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                    <path d="M6 6.742L18 6.742" fill="none" stroke="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                    <path d="M6 17.242L18 17.242" fill="none" stroke="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                    <path d="M21 11.992L23.25 11.992" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                    <path d="M20.25 3.742L21.75 2.242" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                    <path d="M20.25 20.242L21.75 21.742" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                    <path d="M3 11.992L0.75 11.992" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                    <path d="M3.75 3.742L2.25 2.242" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                    <path d="M3.75 20.242L2.25 21.742" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                    </g></svg>
                <span class="bottom-callout__feature-text">
                    Get the most out of your learning
                </span>
            </li>
            <li class="bottom-callout__feature">
                <svg class="bottom-callout__feature-icon hover-blue" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <g transform="matrix(1,0,0,1,0,0)">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12.095V17.845H9V12.095"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M7.5 13.345L12 9.59497L16.5 13.345"></path>
                    <path fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15.75 4.5H19.5C19.8978 4.5 20.2794 4.65804 20.5607 4.93934C20.842 5.22064 21 5.60218 21 6V21.75C21 22.1478 20.842 22.5294 20.5607 22.8107C20.2794 23.092 19.8978 23.25 19.5 23.25H4.5C4.10218 23.25 3.72064 23.092 3.43934 22.8107C3.15804 22.5294 3 22.1478 3 21.75V6C3 5.60218 3.15804 5.22064 3.43934 4.93934C3.72064 4.65804 4.10218 4.5 4.5 4.5H8.25C8.25 3.50544 8.64509 2.55161 9.34835 1.84835C10.0516 1.14509 11.0054 0.75 12 0.75C12.9946 0.75 13.9484 1.14509 14.6517 1.84835C15.3549 2.55161 15.75 3.50544 15.75 4.5V4.5Z"></path>
                    <path fill="none" stroke-width="1.5" d="M12 4.5C11.7929 4.5 11.625 4.33211 11.625 4.125C11.625 3.91789 11.7929 3.75 12 3.75"></path>
                    <path fill="none" stroke-width="1.5" d="M12 4.5C12.2071 4.5 12.375 4.33211 12.375 4.125C12.375 3.91789 12.2071 3.75 12 3.75"></path>
                    </g></svg>
                <span class="bottom-callout__feature-text">
                    Build a portfolio of projects
                </span>
            </li>
            <li class="bottom-callout__feature">
                <svg class="bottom-callout__feature-icon hover-gold" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <g transform="matrix(1,0,0,1,0,0)"><defs><style>.a{fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:1.5px;}.white{stroke:#ffffff;}</style></defs>
                <circle class="a white" cx="4.174" cy="9.571" r="2.446"></circle>
                <circle class="a white" cx="19.826" cy="9.571" r="2.446"></circle>
                <path class="a white" d="M16.4,23.125V16.391a6.347,6.347,0,0,1-5.441-4.32l-.842-2.525a1.468,1.468,0,0,1,1.167-1.915,1.523,1.523,0,0,1,1.642,1.062l.818,2.453a3.42,3.42,0,0,0,3.247,2.338l4.3,0a1.956,1.956,0,0,1,1.958,1.956v7.689"></path>
                <path class="a white" d="M10.453,10.548l-.2.594A3.424,3.424,0,0,1,7,13.484l-4.295,0A1.956,1.956,0,0,0,.75,15.436v7.689"></path>
                <path class="a white" d="M7.6,23.125V16.391A6.347,6.347,0,0,0,12,14"></path>
                <line class="a" x1="11.5" y1="0.875" x2="11.5" y2="2.875"></line>
                <line class="a" x1="15.414" y1="2.961" x2="14" y2="4.375"></line>
                <line class="a" x1="7.586" y1="2.961" x2="9" y2="4.375"></line>
                </g></svg>
                <span class="bottom-callout__feature-text">
                    Get one-on-one help from a real person
                </span>
            </li>
        </ul>
        <p class="bottom-callout__text">
            <a href="https://go.tecla.do/web-dev-course-sale" class="bottom-callout__link">
                Get the video course <svg class="bottom-callout__feature-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><g transform="matrix(1,0,0,1,0,0)"><path d="M10.5,9.121h6V6.011c0-.272.163-.343.362-.158L23,11.54a.751.751,0,0,1-.017,1.142l-6.116,5.336c-.2.185-.362.114-.362-.157v-2.74h-6" fill="none"  stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M7.5 9.121L5.25 9.121" fill="none"  stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M3 9.121L0.75 9.121" fill="none"  stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M7.5 15.121L5.25 15.121" fill="none"  stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M3 15.121L0.75 15.121" fill="none"  stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></g></svg>
            </a>
        </p>
        </div>
    </div>
</template>

<style>
    .bottom-callout {
        background-color: #1c2023;
        color: white;
        stroke: white;
        border-radius: 6px;
        padding: 1rem 1rem 2rem 3rem;
        margin-bottom: 3rem;
        margin-top: 2rem;
    }
    .bottom-callout__content {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .bottom-callout__title {
        font-size: 1.8rem;
        line-height: 1.5em;
        font-weight: 900;
        margin-bottom: 1rem;
        margin-top: 1rem;
    }
    .bottom-callout__text {
        font-size: 1.2rem;
        margin-bottom: 1rem;
    }
    .bottom-callout__features {
        font-size: 1.2rem;
        margin: 0;
        padding: 0;
        margin-left: 1rem;
        margin-top: 1rem;
        margin-bottom: 1rem;
        list-style: none;
    }
    .bottom-callout__feature {
        display: flex;
        align-items: center;
        padding: 0;
        margin: 0;
        margin-bottom: 1em;
    }
    .bottom-callout__feature-icon {
        width: 1.5em;
        height: 1.5em;
        margin-right: 0.75em;
    }
    .bottom-callout__text {
        display: flex;
        justify-content: flex-start;
        margin-top: 0.5rem;
    }
    .bottom-callout__link {
        display: flex;
        align-items: center;
        padding: 1rem 3rem;
        text-decoration: none !important;
        border-radius: 3rem;
        font-weight: 500;
        border: none;
        cursor: pointer;
        background-color: #50e3c2;
        color: #1c2023;
        stroke: #1c2023;
    }
    .bottom-callout__link:hover {
        background-color: #76ecd3;
    }
    .bottom-callout__link .bottom-callout__feature-icon {
        margin-left: 1rem;
        transform: translateY(2px);
    }
    .hover-green:hover {
        fill: #50e3c2;
    }
    .hover-gold:hover {
        stroke: #fcff38;
    }
    .hover-blue:hover {
        fill: #0d78ca;
    }
    @media (max-width: 768px) {
        .bottom-callout {
            padding: 1.5rem;
        }
        .bottom-callout__title {
            margin-top: 0;
            font-size: 1.4rem;
        }
        .bottom-callout__features, .bottom-callout__text {
            font-size: 1rem;
        }
        .bottom-callout__features {
            margin-left: 0;
        }
    }
</style>