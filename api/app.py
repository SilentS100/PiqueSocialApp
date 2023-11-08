from web3 import Web3
import os
import random
import string
import time
import discord
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
from flask import Flask, render_template, Response, request, redirect, url_for, jsonify, json


app = Flask(__name__)

from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

@app.route("/")
def blank():
	return render_template('page.html')

