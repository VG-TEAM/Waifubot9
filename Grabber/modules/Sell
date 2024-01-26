from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from Grabber import application, user_collection

# Assume you have these imports
# from Grabber import collection, user_collection, application

async def sell(update: Update, context: CallbackContext) -> None:
    # Check if the command includes a character ID
    if len(context.args) != 1:
        await update.message.reply_text("Please provide a valid character ID to sell.")
        return

    # Assuming the character ID is provided as an argument
    character_id = context.args[0]
    user_id = update.effective_user.id

    # Retrieve user data from the database (replace this with your actual database query)
    user_data = await user_collection.find_one({'id': user_id, 'characters.id': character_id})

    if not user_data:
        await update.message.reply_text("Character not found in your collection.")
        return

    # Assuming each character is worth 10 coins
    coins_earned = 10

    # Deduct coins from the user's balance (replace this with your actual update logic)
    await user_collection.update_one({'id': user_id}, {'$inc': {'balance': coins_earned}})

    # Remove the sold character from the user's collection (replace this with your actual update logic)
    await user_collection.update_one({'id': user_id}, {'$pull': {'characters': {'id': character_id}}})

    await update.message.reply_text(f"Sold character with ID {character_id} for {coins_earned} coins. "
                                     f"Your new balance is: 💵{user_data['balance'] + coins_earned} coins.")

# Add the balance and sell command handlers to your application
sell_handler = CommandHandler("sell", sell, block=False)

application.add_handler(sell_handler)
