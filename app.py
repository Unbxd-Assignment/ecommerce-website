from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_restful import Api, Resource
import os
import json

app = Flask(__name__)